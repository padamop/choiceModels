library("mlogit")
data("Train", package="mlogit")
Tr <- mlogit.data(Train, shape="wide", choice="choice",
                     varying=4:11, sep="", alt.levels=c(1,2), id="id")
ml.Train <- mlogit(choice~price+time+change+comfort | -1, Tr)
summary(ml.Train)