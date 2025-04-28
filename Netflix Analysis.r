library(ggplot2)
library(dplyr)

# Load data
netflix <- read.csv('Netflix_shows_movies.csv') %>%
  mutate(
    rating = ifelse(is.na(rating), names(which.max(table(rating))), rating)
  )

# Create the plot
p <- ggplot(netflix, aes(x = factor(rating))) +
  geom_bar(fill = 'steelblue') +
  labs(title = 'Distribution of Ratings on Netflix', x = 'Rating', y = 'Count') +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Show the plot in RStudio Viewer or Plot window
print(p)

# Save the plot
ggsave('ratings_distribution_r.png', plot = p, width = 8, height = 6)

