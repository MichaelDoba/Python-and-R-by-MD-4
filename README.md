# 📺 Netflix Data Analysis and Visualization Project
Developer: Michael Doba

## 📚 Assignment Overview
This project uses Python and R to analyze a Netflix dataset, focusing on cleaning, exploration, statistical analysis, and visualizations.

### It covers all the following tasks:

Data Preparation: Extracting and renaming the dataset.

Data Cleaning: Handling missing values properly.

Data Exploration: Summarizing and statistically analyzing key features.

Data Visualization: Plotting most-watched genres and ratings distributions.

R Integration: Replicating a ratings distribution plot in R.

## 🚀 How to Run the Project
Python Analysis
Install required Python libraries:

bash
Copy
Edit
pip install pandas matplotlib seaborn scikit-learn
Run the main script:

bash
Copy
Edit
python netflix_analysis.py
### This will:

~ Unzip and extract the dataset

~ Clean missing values

~ Analyze genres, countries, ratings, durations

~ Generate all visualizations in the outputs/ folder

### R Visualization
Open rating_plot.R in RStudio.

### Install required R libraries if needed:

R
Copy
Edit
install.packages("ggplot2")
install.packages("dplyr")
Run the script.
This will generate a Ratings Distribution bar plot and save it as ratings_distribution_r.png.

## 📊 Detailed Assignment Answers
#### 1. Data Preparation
Task: Unzip and rename.

Work Done:
The Python script automatically unzips the netflix_data.zip file and renames the extracted file to Netflix_shows_movies.csv.

#### 2. Data Cleaning
Task: Address missing values.

Work Done:

Replaced missing director, cast, and country values with "Unknown."

Filled missing rating with the most common rating (mode).

Dropped rows missing the date_added field.

Saved cleaned dataset as Netflix_shows_movies_clean.csv.

#### 3. Data Exploration
Task: Descriptive statistics and exploration.

Work Done:

Summarized content type distributions (Movies vs TV Shows).

Analyzed top countries producing Netflix content.

Explored the distribution of ratings across content.

Analyzed the number of seasons for TV shows and movie durations.

#### 4. Data Visualizations
(Python Visuals)
Most Watched Genres:
top_genres.png → Top 20 genres bar plot.

✔ Ratings Distribution:
Ratings_Distrubution.png → Ratings bar plot.
✔ Genre Co-occurrence:
genre_cooccurrence_heatmap.png → Heatmap of genres appearing together.
✔ Content Type by Country:
country_distribution_heatmap.png → Heatmap showing Movies vs TV Shows by top countries.
✔ Movie Duration:
movie_duration_distribution.png → Histogram of movie lengths.
✔ TV Show Seasons:
tvshow_seasons_distribution.png → Count plot of TV show seasons.
✔ Ratings by Country:
rating_by_country_heatmap.png → Heatmap showing ratings across countries.
✔ Ratings by Content Type:
rating_by_type_stacked.png → Stacked bar plot.

#### (R Visual)
✔ Ratings Distribution:
ratings_distribution_r.png → Bar plot showing counts per rating category.

## 💾 Outputs Location
All outputs (plots and visualizations) are saved automatically into the outputs/ folder inside the project.

## 🛠 Requirements
Python 3.7+: with pandas, matplotlib, seaborn, scikit-learn

R and RStudio (Optional for R script)

## ✨ Final Notes
Code adheres to clean Python standards.

Includes full error handling (e.g., missing files, loading issues).

Both Python and R integrations are completed as per the assignment.

Full project ready for submission as a ZIP file or GitHub Repository.

## ✅ Submission Checklist
✔ Python script for full analysis
✔ R script for Ratings Distribution visualization
✔ Cleaned dataset
✔ All generated plots
✔ Comprehensive README file
✔ Folder structured and organized

## 👨‍💻 Author
Michael Doba
Netflix Data Analysis Project
