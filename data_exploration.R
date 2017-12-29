library(ggplot2)  
library(ggthemes) 
UCI_Crecard <- read.csv(file.choose())
str(UCI_Crecard)
dim(UCI_Crecard)
summary(UCI_Crecard)

UCI_Crecard$AGE<-cut(UCI_Crecard$AGE, breaks = c( 10, 30,50,100), labels = c("young", "middle","senior"))
UCI_Crecard$SEX<-cut(UCI_Crecard$SEX, 2,labels = c("Female","Male"))
UCI_Crecard$MARRIAGE<-cut(UCI_Crecard$MARRIAGE, 4,labels = c("married","single","Devorce","other"))
convertcat <- c(3:5)
UCI_Crecard[,convertcat] <- data.frame(apply(UCI_Crecard[convertcat],2, as.factor))
UCI_Crecard$default.payment.next.month<-as.factor(UCI_Crecard$default.payment.next.month)
# ggplot boxplot for age ,limit bal and default-payment
ggplot(data=UCI_Crecard,mapping = aes(x=AGE,y=UCI_Crecard$LIMIT_BAL,fill=default.payment.next.month)) + geom_boxplot() 



#marriage
ggplot(data=UCI_Crecard, mapping = aes(x=MARRIAGE, fill=default.payment.next.month)) + geom_bar()
#sex
ggplot(data=UCI_Crecard, mapping = aes(x=SEX, fill=default.payment.next.month)) + geom_bar()
#education
ggplot(data=UCI_Crecard,mapping = aes(x=EDUCATION,y=UCI_Crecard$LIMIT_BAL,fill=default.payment.next.month)) + geom_boxplot()

UCI_Crecard$PAY_0<-as.numeric(UCI_Crecard$PAY_0)
UCI_Crecard$PAY_2<-as.numeric(UCI_Crecard$PAY_2)
UCI_Crecard$PAY_3<-as.numeric(UCI_Crecard$PAY_3)
UCI_Crecard$PAY_4<-as.numeric(UCI_Crecard$PAY_4)
UCI_Crecard$PAY_5<-as.numeric(UCI_Crecard$PAY_5)
UCI_Crecard$PAY_6<-as.numeric(UCI_Crecard$PAY_6)


correlationMatrix <- cor(UCI_Crecard[,8:24])
print(correlationMatrix)
