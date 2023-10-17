Pila <- list()
push <- function(Pila, elemento){
  +     pila <- c(Pila, elemento)
  +     return(Pila)
}
pop <- function(Pila){
  +     if(length(Pila)>0){
    +         elemento <- Pila[length(Pila)]
    +         Pila <- Pila[length(Pila)]
    +         return(lista(elemento, Pila))
    +     }else{
      +         return("Lista vacia")
      +     }
  + }
MiPila <- list()
MiPila <- push(MiPila, 0)
elemento <- pop(MiPila)