## generate the true model
beta_price_blue = -0.75
beta_price_red = -0.5
beta_price_out = 0
alpha_blue = 3.584
alpha_red = 1.99
alpha_out = 0

#prices = 0:10
#prices = prices*0.25

#pBlue = 6
#pRed = 5

#plot(0,0, col='white', xlim = c(0, 10), ylim=c(0,1), las=1, xlab='prices blue cars', ylab='expected sales', main='simpler model makes better predictions')
## draw the true model lines
#y0 = log(0.2/0.5)
#x0 = pBlue
#slope_blue = beta_price_blue
#intercept_blue = y0 - slope_blue*x0

#y0 = log(0.3/0.5)
#x0 = pRed
#slope_red = beta_price_red
#intercept_red = y0 - slope_red*x0

#yTrue <- 1 - 1/(1 + exp(intercept_blue + slope_blue*prices))

#relGreen = c()
#relPink = c()

# for random prices, fit models and draw the corresponding lines
for(i in 1:100){
  # random prices
  pRed = runif(1, 0, 10)
  pBlue = runif(1, 0, 10)
  
  uRed = alpha_red + beta_price_red*pRed
  uBlue = alpha_blue + beta_price_blue*pBlue
  uOut = 0
  
  #uRed = intercept_red + slope_red*pRed
  #uBlue = intercept_blue + slope_blue*pBlue
  
  #slopeRed = uRed/pRed
  #slopeBlue = uBlue/pBlue
  
  # draw the spline
  #	y <- 1 - 1/(1 + exp(slopeRed*prices) + exp(slopeBlue*prices))
  #y <- 1 - 1/(1 + exp(slopeBlue*prices))
  #tmpRelPink = abs(yTrue - y)/yTrue
  #relPink <- c(relPink, tmpRelPink)
  #lines(spline(prices, y), col='pink', lwd=0.5)
  
  # simpler model
  #f <- function(beta, pRed, pBlue, yRed, yBlue) (pRed*yRed + pBlue*yBlue)*(1 + exp(beta*pRed) + 			exp(pBlue*beta)) - pRed*exp(beta*pRed) - pBlue*exp(beta*pBlue)
  yRed = exp(uRed)/(1 + exp(uRed) + exp(uBlue))
  yBlue = exp(uBlue)/(1 + exp(uRed) + exp(uBlue))
  #beta = uniroot(f, lower=-10, upper=10, tol=1e-10, pRed=pRed, pBlue=pBlue, yRed=yRed, yBlue=yBlue)
  #slope = beta$root
  #	y <- 1 - 1/(1 + exp(slope*prices) + exp(slope*prices))
  #y <- 1 - 1/(1 + exp(slope*prices))
  #tmpRelGreen = abs(yTrue - y)/yTrue
  #relGreen <- c(relGreen, tmpRelGreen)
  #lines(spline(prices, y), col='lightgreen', lwd=0.5)
}
# draw the line corresponding to the true model
#y <- 1 - 1/(1 + exp(intercept_red + slope_red*prices) + exp(intercept_blue + slope_blue*prices))
#y <- 1 - 1/(1 + exp(intercept_blue + slope_blue*prices))
#plot(prices, y)
#lines(spline(prices, y))
#summary(relGreen)
#summary(relPink)

# plot the histograms of the relative errors
b = seq(0, 70, 0.5)
hist(relGreen,breaks=b, col='lightgreen', probability=T, border='white', xlab='relative error', ylab='', main='', xlim=c(0,10), las=1)
hist(relPink,breaks=b, col=rgb(1, 0, 0, 0.5), probability=T, border='white', xlab='relative error', ylab='', main='', xlim=c(0,10), add=T)
greenMean = mean(relGreen)
pinkMean = mean(relPink)
greenMedian = median(relGreen)
pinkMedian = median(relPink)

sm_green = sprintf('%.2f', greenMean)
sm_pink = sprintf('%.2f', pinkMean)
sd_green = sprintf('%.2f', greenMedian)
sd_pink = sprintf('%.2f', pinkMedian)
text(5, 0.5, "Mean")
text(5, 0.45, "Median")
text(6.5, 0.55, "Model M2")
text(8.5, 0.55, "Model M3")
text(6.5, 0.5, sm_green, col='darkgreen')
text(6.5, 0.45, sd_green, col='darkgreen')
text(8.5, 0.5, sm_pink, col='darkred')
text(8.5, 0.45, sd_pink, col='darkred')