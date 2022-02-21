library(ggplot2)
ggram(c("hacker", "programmer"), year_start = 1950)
# Changing the geom.
ggram(c("cancer", "fumer", "cigarette"),
      year_start = 1900,
      corpus = "fre_2012",
      smoothing = 0,
      geom = "step")
# Passing more options.
ggram(c("cancer", "smoking", "tobacco"),
      year_start = 1900,
      corpus = "eng_fiction_2012",
      geom = "point",
      smoothing = 0,
      geom_options = list(alpha = .5)) +
  stat_smooth(method="loess", se = FALSE, formula = y ~ x)
# Setting the layers manually.
ggram(c("cancer", "smoking", "tobacco"),
      year_start = 1900,
      corpus = "eng_fiction_2012",
      smoothing = 0,
      geom = NULL) +
  stat_smooth(method="loess", se=FALSE, span = 0.3, formula = y ~ x)
# Setting the legend placement on a long query and using the Google theme.
# Example taken from a post by Ben Zimmer at Language Log.
p <- c("((The United States is + The United States has) / The United States)",
       "((The United States are + The United States have) / The United States)")
ggram(p, year_start = 1800, google_theme = TRUE) +
  theme(legend.direction="vertical")
# Pass ngram data rather than phrases
ggram(hacker) + facet_wrap(~ Corpus)