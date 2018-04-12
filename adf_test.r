library(zoo)
library(tseries)
#gld <- read.csv("price_taibao.csv", stringsAsFactors=F)

#gld <- read.csv("price_AGRI.csv", stringsAsFactors=F)
#gdx <- read.csv("price_ICBC.csv", stringsAsFactors=F)

gld <- read.csv("price_try1.csv", stringsAsFactors=F)
gdx <- read.csv("price_try2.csv", stringsAsFactors=F)

gld <- zoo(gld[,4], as.Date(gld[,2]))
gdx <- zoo(gdx[,4], as.Date(gdx[,2]))

t.zoo <- merge(gld, gdx, all=FALSE)
t <- as.data.frame(t.zoo)

cat("Date range is", format(start(t.zoo)), "to", format(end(t.zoo)), "\n")

m <- lm(gld ~ gdx + 0, data=t)
beta <- coef(m)[1]

cat("Assumed hedge ratio is", beta, "\n")

sprd <- t$gld - beta*t$gdx
ht <- adf.test(sprd, alternative="stationary", k=0)

cat("ADF p-value is", ht$p.value, "\n")

if (ht$p.value < 0.05) {
  cat("The spread is likely mean-reverting\n")
} else {
  cat("The spread is not mean-reverting.\n")
}
