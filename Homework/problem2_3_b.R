# Choice Models in Operations
# Homework 2

# Load library
library("mlogit")

# Where I store my files
setwd("F:\\Dropbox\\NYU\\2012 Fall\\Choice Models in Operations\\Homework\\Homework2\\")

# part (b)
# Read data
mydata <- read.table("data_frame.txt", sep = "\t", col.names=c( 'id', 'choiceid', 'p1', 'p2'))

# Shape a data.frame in a suitable form for the use of the mlogit function
ml.data <- mlogit.data(mydata, shape="wide", choice="choiceid",
                  varying=3:4, sep="", alt.levels=c(1,2), id="id")

# V_j = b * p_j
# Estimation by maximum likelihood of the multinomial logit model, with alternative-specific and/or individual specific variables.
ml.results1 <- mlogit(choiceid~p | +0, data = ml.data)
# Result summaries
summary(ml.results1)

# V_j = a_j + b * p_j with one of the a_j set to zero
ml.results2 <- mlogit(choiceid~p, data = ml.data, reflevel="1")
summary(ml.results2)

# V_j = d_j * p_j
ml.results3 <- mlogit(choiceid~+0 | +0 | p , data = ml.data)
summary(ml.results3)


# Repeat with b = -0.2
mydata <- read.table("data_frame2.txt", sep = "\t", col.names=c( 'id', 'choiceid', 'p1', 'p2'))

ml.data <- mlogit.data(mydata, shape="wide", choice="choiceid",
                       varying=3:4, sep="", alt.levels=c(1,2), id="id")

# V_j = b * p_j
ml.results1 <- mlogit(choiceid~p | +0, data = ml.data)
summary(ml.results1)

# V_j = a_j + b * p_j with one of the a_j set to zero
ml.results2 <- mlogit(choiceid~p, data = ml.data, reflevel="1")
summary(ml.results2)

# V_j = d_j * p_j
ml.results3 <- mlogit(choiceid~+0 | +0 | p , data = ml.data)
summary(ml.results3)


# Repeat with b = -0.2 and no-purchase option
mydata <- read.table("data_frame3.txt", sep = "\t", col.names=c( 'id', 'choiceid', 'p0', 'p1', 'p2'))

ml.data <- mlogit.data(mydata, shape="wide", choice="choiceid",
                       varying=3:5, sep="", alt.levels=c(1,2,3), id="id")

# V_j = b * p_j
ml.results1 <- mlogit(choiceid~p | +0, data = ml.data)
summary(ml.results1)

# V_j = a_j + b * p_j with one of the a_j set to zero
ml.results2 <- mlogit(choiceid~p, data = ml.data, reflevel="1")
summary(ml.results2)

# V_j = d_j * p_j
ml.results3 <- mlogit(choiceid~+0 | +0 | p , data = ml.data)
summary(ml.results3)




# part (c)
mydata <- read.table("data_frame4.txt", sep = "\t", col.names=c( 'id', 'choiceid', 'p0', 'p1', 'p2'))

ml.data <- mlogit.data(mydata, shape="wide", choice="choiceid",
                       varying=3:5, sep="", alt.levels=c(1,2,3), id="id")

# V_j = b * p_j
ml.results1 <- mlogit(choiceid~p | +0, data = ml.data)
summary(ml.results1)

# V_j = d_j * p_j
ml.results3 <- mlogit(choiceid~+0 | +0 | p , data = ml.data)
summary(ml.results3)