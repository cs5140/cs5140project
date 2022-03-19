install.packages("ngramr")
ngramr::ggram("memes")
library(ggplot2)
ngramr::ggram(c("hacker", "programmer"), year_start = 1950)
# Changing the geom.
ngramr::ggram(c("cancer", "fumer", "cigarette"),
      year_start = 1900,
      corpus = "fre_2012",
      smoothing = 0,
      geom = "step")
# Passing more options.
ngramr::ggram(c("cancer", "smoking", "tobacco"),
      year_start = 1900,
      corpus = "eng_fiction_2012",
      geom = "point",
      smoothing = 0,
      geom_options = list(alpha = .5)) +
  stat_smooth(method="loess", se = FALSE, formula = y ~ x)
# Setting the layers manually.
ngramr::ggram(c("cancer", "smoking", "tobacco"),
      year_start = 1900,
      corpus = "eng_fiction_2012",
      smoothing = 0,
      geom = NULL) +
  stat_smooth(method="loess", se=FALSE, span = 0.3, formula = y ~ x)
# Setting the legend placement on a long query and using the Google theme.
# Example taken from a post by Ben Zimmer at Language Log.
p <- c("((The United States is + The United States has) / The United States)",
       "((The United States are + The United States have) / The United States)")
ngramr::ggram(p, year_start = 1800, google_theme = TRUE) +
  theme(legend.direction="vertical")
# Pass ngram data rather than phrases
ngramr::ggram(hacker) + facet_wrap(~ Corpus)

#
x = ngramr::ngram("corporatocracy", corpus = "eng_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
y = ngramr::ngram("corporatocracy", corpus = "eng_fiction_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)

plot(x$Year,x$Frequency, type="l",col="red")
lines(x$Year,y$Frequency,col="green")

plot(x$Year,x$Frequency, type="l",col="red")
lines(x$Year,x$Frequency-y$Frequency,col="blue")

plot(x$Year,y$Frequency, type="l",col="red")
lines(x$Year,x$Frequency-y$Frequency,col="blue")

x = ngramr::ngram("dark arts", corpus = "eng_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
df <- data.frame(Year = c(x$Year),
                 Freq = c(x$Frequency),
                 Count = c(x$Count)
)
write.csv(df,"/Users/scottk/PycharmProjects/MachineLearning/textfiles/mlwords/x.csv", row.names = FALSE)

y = ngramr::ngram("dark art", corpus = "eng_fiction_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
plot(x$Year,x$Count, type="l",col="red")
lines(x$Year,y$Count, col="green")

data <- read.csv(file = "words.csv", header = FALSE)
for(line in data){
  print(line)
  x = ngramr::ngram(line, corpus = "eng_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
  y = ngramr::ngram(line, corpus = "eng_fiction_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
#  plot(x$Year,x$Count, type="l",col="red")
#  lines(x$Year,y$Count, col="green")
  df <- data.frame(Year = c(x$Year),
                   Freq = c(x$Frequency),
                   Count = c(x$Count)
  )
  write.csv(df,paste("/Users/scottk/PycharmProjects/MachineLearning/textfiles/mlwords/",line,"_norm.csv",sep=""), row.names = FALSE)
  df <- data.frame(Year = c(y$Year),
                   Freq = c(y$Frequency),
                   Count = c(y$Count)
  )
  write.csv(df,"/Users/scottk/PycharmProjects/MachineLearning/textfiles/mlwords/"+line+"_fict.csv", row.names = FALSE)
}