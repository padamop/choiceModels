library("mlogit")
data("Train", package="mlogit")
Tr <- mlogit.data(Train, shape="wide", choice="choice",
                     varying=4:11, sep="", alt.levels=c(1,2), id="id")
ml.Train <- mlogit(choice~price+time+change+comfort | -1, Tr)
summary(ml.Train)

# We now convert price and time in more meaningful unities, hours and euros (1 guilder is 2:20371 euros) :
Tr$price <- Tr$price / 100 * 2.20371
Tr$time <- Tr$time / 60
ml.Train <- mlogit(choice~price+time+change+comfort | -1, Tr)
#summary(ml.Train)
# The coecients are not directly interpretable, but dividing them by the price coecient, we get monetary values :
coef(ml.Train)[-1]/coef(ml.Train)[1]