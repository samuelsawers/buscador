import sys
 
class Progreso:
        '''
                Muestra una barra de progreso que se actualiza en una misma linea. Ejemplo de uso:
                from progreso import Progreso
                import time
 
                titulo = "Analizando"
                carCompletado = '#'
                carVacio = '_'
                tamBarra = 50
 
                barra = Progreso(titulo, carCompletado, carVacio, tamBarra)
 
                veces = 20
                for i in range(veces):
                        time.sleep(0.5)
                        barra.actualizarBarra(float(i+1)/veces*100)
        '''
        def __init__ (self, tit, carCom, carVac, tamBarra):
                self.titulo=tit
                self.carCompletado=carCom
                self.carVacio=carVac
                self.tamBarra=tamBarra
                self.progreso=0
               
                sys.stdout.write(self.titulo + ": [" + self.carVacio *self.tamBarra + "]" + chr(8)*(self.tamBarra+1))
                sys.stdout.flush()
                self.progreso = 0
               
        def actualizarBarra(self, x):
                celdas = int(x)*self.tamBarra//100
                sys.stdout.write(self.carCompletado*(celdas - self.progreso))
                sys.stdout.flush()
                self.progreso = celdas