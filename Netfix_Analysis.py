# ==================================================================
# NETFLIX Data Cleaning, Data Exploration, Data Analysis and Data
# Visualisation by Michael Doba
# ==================================================================

import zipfile
import os

# Raw Data and Extracted Data Paths
raw_data_path = r'C:\Users\mdoba\OneDrive - Population Services International\Documents\Netflix assignment 4\data\raw\netflix_data.zip'
extracted_dir = r'C:\Users\mdoba\OneDrive - Population Services International\Documents\Netflix assignment 4'

# Ensuring extraction directory exists
os.makedirs(extracted_dir, exist_ok=True)

# Checking if ZIP exists
if not os.path.exists(raw_data_path):
    print(f"Error: ZIP file not found at {raw_data_path}")
    exit()

try:
    # Extracting ZIP
    with zipfile.ZipFile(raw_data_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_dir)
    print("ZIP file have been extracted successfully.")

    # Renaming the extracted CSV (adjust original filename)
    original_file = os.path.join(extracted_dir, "netflix_data.csv")  # Replace with your CSV's name
    new_file = os.path.join(extracted_dir, "Netflix_shows_movies.csv")

    if os.path.exists(original_file):
        os.rename(original_file, new_file)
        print("Extracted File renamed successifully")
        print(f"Renamed file to {new_file}")
    else:
        print(f"Error: Extracted file {original_file} not found.")

except Exception as e:
    print("Error while extracting ZIP file:",e)

import pandas as pd

# Path to your CSV file
csv_path = r'C:\Users\mdoba\OneDrive - Population Services International\Documents\Netflix assignment 4\Netflix_shows_movies.csv'
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    print(f"Error:File not found at {csv_path}. Check the path or unzip the dataset first.")
    exit()

# Handling missing values correctly
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df = df.dropna(subset=['date_added'])  # Remove rows with missing date_added

# Save cleaned data
df.to_csv("Netflix_shows_movies_clean.csv", index=False)
print("Cleaned data saved!")

# Verify
print("\nMissing value after cleaning")
print(df.isnull().sum())

# Content Type Distribution (Movies vs. TV Shows)
print("\nContent Type Distribution (Movies vs. TV Shows)")
print(df['type'].value_counts())

# Top 10 Countries
print("\nTop 10 Countries")
print(df['country'].value_counts().head(10))

# Ratings Summary
print("\nRatings Summary")
print(df['rating'].value_counts())

import matplotlib.pyplot as plt
from pathlib import Path

# Defining the correct file path
current_dir = Path(__file__).parent  # Gets directory where script is located
csv_path = current_dir / "Netflix_shows_movies.csv"  # Looks for CSV in same folder as script

# Verifying the file existance
if not csv_path.exists():
    print(f"ERROR: File not found at {csv_path}")
    print("Please ensure:")
    print(f"1. The file 'Netflix_shows_movies.csv' exists in {current_dir}")
    print("2. Or update the path in the script to match your file location")
    print("Current working directory:", os.getcwd())
    print("Files in directory:", os.listdir())
    exit()

# Loading the data
try:
    df = pd.read_csv(csv_path)
    print("Data loaded successfully! Found", len(df), "records")
except Exception as e:
    print("Failed to load CSV:", e)
    exit()

# ==================================================================
# GENRE ANALYSIS
# ==================================================================

# Clean and prepare genre data
df['listed_in'] = df['listed_in'].str.strip()  # Remove whitespace
all_genres = df['listed_in'].str.split(', ').explode()

# Create outputs folder if it doesn't exist
output_dir = current_dir / "outputs"
output_dir.mkdir(exist_ok=True)

# Individual Genre Frequency (Top 15)
plt.figure(figsize=(12, 8))
genre_counts = all_genres.value_counts().head(20)
genre_counts.sort_values().plot(kind='barh', color='darkred')
plt.title('Top 20 Most Common Genres')
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig(output_dir / 'top_genres.png', dpi=120)
plt.show()

print("\nAnalysis complete for Individual Genre Frequency! Check the 'outputs' folder for visualizations.")

#GENRE CO-OCCURRENCE HEATMAP (Top 15 genres)

import seaborn as sns # type: ignore
from sklearn.preprocessing import MultiLabelBinarizer  # For genre co-occurrence

# Process genres
df['genre_list'] = df['listed_in'].str.split(', ')
top_genres = df['genre_list'].explode().value_counts().head(15).index.tolist()

# Create co-occurrence matrix
mlb = MultiLabelBinarizer()
genre_matrix = pd.DataFrame(mlb.fit_transform(df['genre_list']),
                           columns=mlb.classes_,
                           index=df.index)
top_genre_matrix = genre_matrix[top_genres]
cooccurrence = top_genre_matrix.T.dot(top_genre_matrix)

# Plot heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(cooccurrence, cmap='Purples', annot=True, fmt='g',
           linewidths=.5, cbar_kws={'label': 'Co-occurrence Count'})
plt.title('Genre Co-occurrence Heatmap (Top 15 Genres)')
plt.tight_layout()
plt.savefig(output_dir / 'genre_cooccurrence_heatmap.png', dpi=120)
plt.show()

print("\nEnhanced Analysis for Genre complete! Check the 'outputs' folder for all visualizations.")

# ==================================================================
# CONTENT TYPE DISTRUBUTION ANALYSIS
# ==================================================================

df = pd.read_csv("Netflix_shows_movies_clean.csv")

# Plot Movies vs. TV shows
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df, hue='type', palette='pastel', legend=False)
plt.title('Movies vs. TV Shows on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.savefig(output_dir / 'Content_type_distrubution.png', dpi=120)
plt.show()

print("\nAnalysis complete for Content_Type_Distrubution! Check the 'outputs' folder for visualizations.")

# COUNTRY-WISE CONTENT DISTRIBUTION HEATMAP (Top 15 countries)
top_countries = df['country'].value_counts().head(15).index
country_type_data = df[df['country'].isin(top_countries)].groupby(
    ['country', 'type']).size().unstack().fillna(0)
plt.figure(figsize=(12, 8))
sns.heatmap(country_type_data, cmap='Greens', annot=True, fmt='g',
           linewidths=.5, cbar_kws={'label': 'Number of Titles'})
plt.title('Content Distribution by Country and Type (Top 15 Countries)')
plt.xlabel('Content Type')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig(output_dir / 'country_distribution_heatmap.png', dpi=120)
plt.show()

print("\nAnalysis complete for Countrywise Content_Type_Distrubution! Check the 'outputs' folder for visualizations.")

# DURATION ANALYSIS FOR MOVIES and TV SHOWS

# Separate movies and TV shows
movies = df[df['type'] == 'Movie'].copy()
tv_shows = df[df['type'] == 'TV Show'].copy()

# Clean duration for movies
movies['duration'] = movies['duration'].str.extract('(\d+)').astype(float)
# For TV shows, we'll use seasons
tv_shows['duration'] = tv_shows['duration'].str.extract('(\d+)').astype(float)

# Movie duration distribution
plt.figure(figsize=(12, 8))
sns.histplot(data=movies, x='duration', bins=30, kde=True, color='skyblue')
plt.title('Distribution of Movie Durations (in minutes)')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig(output_dir / 'movie_duration_distribution.png', dpi=120)
plt.show()

print("\nAnalysis complete for Movies duration! Check the 'outputs' folder for visualizations.")

# TV show seasons distribution
plt.figure(figsize=(12, 8))
sns.countplot(data=tv_shows, x='duration', color='salmon')
plt.title('Distribution of TV Show Seasons')
plt.xlabel('Number of Seasons')
plt.ylabel('Number of TV Shows')
plt.tight_layout()
plt.savefig(output_dir / 'tvshow_seasons_distribution.png', dpi=120)
plt.show()

print("\nAnalysis complete for TV Shows duration! Check the 'outputs' folder for visualizations.")

print("\nEnhanced Analysis for Content Type Distrubution complete! Check the 'outputs' folder for all visualizations.")

# ==================================================================
# RATINGS DISTRUBUTION ANALYSIS
# ==================================================================

# Create output directory if it doesn't exist
os.makedirs('outputs', exist_ok=True)

# Plot Ratings Distribution
plt.figure(figsize=(12, 6))
ratings = df['rating'].value_counts().reset_index()
ratings.columns = ['rating', 'count']

sns.barplot(data=ratings, x='rating', y='count', hue='rating', palette='viridis', legend=False)
plt.title('Distribution of Content Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / 'Ratings_Distrubution.png', dpi=120)
plt.show()

print("\nAnalysis complete for Ratings_Distrubution! Check the 'outputs' folder for visualizations.")

# RATING HEATMAP BY COUNTRY (Top 10 Countries)
top_countries = df['country'].value_counts().head(10).index
rating_country_data = df[df['country'].isin(top_countries)].groupby(
    ['country', 'rating']).size().unstack().fillna(0)

plt.figure(figsize=(14, 8))
sns.heatmap(rating_country_data, cmap='Reds', annot=True, fmt='g',
           linewidths=0.5, cbar_kws={'label': 'Number of Titles'})
plt.title('Rating Distribution Across Top 10 Countries', weight='bold', pad=20)
plt.xlabel('Rating')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig(output_dir / 'rating_by_country_heatmap.png', dpi=120)
plt.show()

print("\nAnalysis complete for Ratings_Heatmap_by_Country! Check the 'outputs' folder for visualizations.")

# RATING DISTRIBUTION BY CONTENT TYPE

rating_by_type = df.groupby(['rating', 'type']).size().unstack()
rating_by_type.plot(kind='bar', stacked=True, color=['#E50914', '#221F1F'])
plt.title('Rating Distribution by Content Type', weight='bold')
plt.xlabel('Rating')
plt.ylabel('Number of Titles')
plt.legend(title='Content Type')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / 'rating_by_type_stacked.png', dpi=120)
plt.show()

print("\nAnalysis complete for Ratings_Distrubution_by_Content_Type! Check the 'outputs' folder for visualizations.")

print("\nEnhanced Ratings analysis complete! Check the 'outputs' folder for new visualizations.")