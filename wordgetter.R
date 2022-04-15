data <- read.csv(file = "new_word.csv", header = FALSE)
for(line in data){
  print(line)
  x = ngramr::ngram(line, corpus = "eng_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
  y = ngramr::ngram(line, corpus = "eng_fiction_2019", count = TRUE, case_ins = TRUE, aggregate = TRUE, smoothing = FALSE)
  df <- data.frame(Year = c(x$Year),
                   Freq = c(x$Frequency),
                   Count = c(x$Count)
  )
  write.csv(df,paste("gotten_wordN.csv"), row.names = FALSE)
  df <- data.frame(Year = c(y$Year),
                   Freq = c(y$Frequency),
                   Count = c(y$Count)
  )
  write.csv(df,"gotten_wordF.csv", row.names = FALSE)
}
