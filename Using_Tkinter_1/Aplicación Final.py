from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

enfermedad=""

imagenes=[]
sintoma_enfermedad=[]

for i in range(26):
    sintoma_enfermedad.append("a")


class enfermedades:
    
    def interface(self,imagen,sintoma,buttonnumber):
        global enfermedad
        enfermedad=Toplevel()
        enfermedad.geometry("500x370+800+100")
        enfermedad.title("diagnostico")
        enfermedad.config(bg="light blue")
        Label(enfermedad, text="Bienvenido al consultorio",font="Baskerville 15",bg="light blue",fg="red").place(x=150,y=10)
        Label(enfermedad,image=imagen[buttonnumber],width=300,height=250,relief=SOLID).place(x=100,y=50)
        Button(enfermedad,text="comenzar con el analisis",command=lambda: self.sintomas(sintoma,buttonnumber)).place(x=190,y=320)
    
    def sintomas(self,sintoma,buttonnumber):
        
        probabilidad=0

        if buttonnumber==0:
            empezar=0
            parar=3
        if buttonnumber==1:
            empezar=3
            parar=6
        if buttonnumber==2:
            empezar=6
            parar=8
        if buttonnumber==3:
            empezar=8
            parar=10
        if buttonnumber==4:
            empezar=10
            parar=12
        if buttonnumber==5:
            empezar=12
            parar=14
        if buttonnumber==6:
            empezar=14
            parar=17
        if buttonnumber==7:
            empezar=17
            parar=20
        if buttonnumber==8:
            empezar=20
            parar=23
        if buttonnumber==9:
            empezar=23
            parar=26


        for i in range(empezar,parar):
            confirmación=messagebox.askyesno(title="sintomas",message=f"""¿Tiene alguno de los siguientes sintomas?
            {sintoma[i]}""")

            if confirmación:
                probabilidad+=30
        
        if probabilidad==0:
            messagebox.showinfo(title="confirmación",message=f"su probabilidad es de {probabilidad}%, se encuentra a salvo de esta enfermedad")
        elif probabilidad<40:
            messagebox.showinfo(title="confirmación",message=f"su probabilidad es de {probabilidad}%, debería hacerse una revisión")
        elif probabilidad<80:
            messagebox.showinfo(title="confirmación",message=f"su probabilidad es de {probabilidad}%, debería hacer una cita con un medio especializado")
        elif probabilidad<100:
            messagebox.showinfo(title="confirmación",message=f"su probabilidad es de {probabilidad}%, busque atención medica lo más pronto posible")
        
        
        
        enfermedad.destroy()
        


raiz=Tk()
raiz.title("Consultorio de Don Pedro")
raiz.iconbitmap("icono.ico")
raiz.geometry("500x550+150+100")
raiz.config(bg="light blue")
raiz.resizable(0,0)

#insertar imagenes en la lista

imagenes.append(ImageTk.PhotoImage(Image.open("Covid.jpg")))#0
imagenes.append(ImageTk.PhotoImage(Image.open("gastritis.jpg")))#1
imagenes.append(ImageTk.PhotoImage(Image.open("tuberculosis-1.jpg")))#2
imagenes.append(ImageTk.PhotoImage(Image.open("insuficiencia renal-3.jpg")))#3
imagenes.append(ImageTk.PhotoImage(Image.open("Diabetes.jpg")))
imagenes.append(ImageTk.PhotoImage(Image.open("Hipertensión.jpg")))
imagenes.append(ImageTk.PhotoImage(Image.open("Pancreatitis.jpg")))
imagenes.append(ImageTk.PhotoImage(Image.open("Hepatitis.jpg")))
imagenes.append(ImageTk.PhotoImage(Image.open("anemia.jpg")))
imagenes.append(ImageTk.PhotoImage(Image.open("calculos.jpg")))

base=enfermedades()



#insertar sintomas

#covid
sintoma_enfermedad[0]=("""
        - Fiebre
        - Tos
        - Cansancio recurrente""")
sintoma_enfermedad[1]=("""
        - Dolor de garganta
        - Diarrea
        - Conjuntivitis
        - Dolor de cabeza
        - Pérdida del sentido del olfato o del gusto
        - Erupciones cutáneas o pérdida del color en los dedos 
        de las manos o de los pies""")
sintoma_enfermedad[2]=("""
        - Dificultad para respirar o sensación de falta de aire
        - Dolor o presión en el pecho
        - Incapacidad para hablar o moverse""")


#gastritis
sintoma_enfermedad[3]=("""
        - dolor o molestia en la parte superior del abdomen
        - sensación de llenura demasiado 
        - pronto durante una comida
        - inapetencia
        - adelgazamiento""")
sintoma_enfermedad[4]=("""
        - náuseas o vómito
        - sangrado de estomago
        - calambres, molestias o dolor en el abdomen
        - sensación de cansancio, falta de aliento o mareo""")
sintoma_enfermedad[5]=("""
        - heces de color negro 
        - heces apariencia de alquitrán 
        - heces con sangre de color rojo o marrón
        - vomito con sangre roja 
        - vómito que parece granos de café""")


#tuberculosis 
sintoma_enfermedad[6]=("""
        - Tos con sangre
        - Pérdida de peso
        - Sudores nocturnos""")
sintoma_enfermedad[7]=("""
        - Fiebre
        - Pérdida de peso sin causa conocida
        - Falta de apetito
        - Sudores nocturnos
        - Tos que dura más de 3 semanas
        - Dolor de pecho""")


#insuficiencia renal
sintoma_enfermedad[8]=("""
        - Menor producción de orina, que puede ser más oscura, o ausencia de orina
        - Mayor necesidad de ir al baño, sobre todo por la noche ((en un menor número de casos, en lugar de menor producción de orina, se produce un aumento de esta))
        - Retención de líquidos: provoca edema o hinchazón de pies o tobillos.
        - Bolsas alrededor de los ojos, sobre todo por la mañana.
        - Boca seca y picores en la piel.""")
sintoma_enfermedad[9]=("""
        - Problemas digestivos: falta de apetito, náuseas, vómitos, gastritis y trastornos en el ritmo intestinal
        - Dificultad para respirar.
        - Somnolencia, cansancio y falta de aliento.
        - Dificultad para pensar con claridad y confusión""")



#diabetes
sintoma_enfermedad[10]=("""
        - orina con frecuencia por las noches
        - sentir mucha sed 
        - entumecimiento/hormigueo en manos o pies
        - bajo de peso sin razón""")

sintoma_enfermedad[11]=(""" 
        - dificultad para la cicatrización de heridas
        - vista borrosa
        - aumento de hambre 
        - cansancio frecuente""")


#hipertensión
sintoma_enfermedad[12]=("""
        - dolor de cabeza
        - ansiedad
        - problemas de sueño""")

sintoma_enfermedad[13]=("""    
        - enrojecimiento 
        - confusión
        - hemorragias nasales""")

#Pancreatitis
sintoma_enfermedad[14]=("""
        - Nauseas
        - Fiebre
        - Vomitos""")
sintoma_enfermedad[15]=("""
        - Sensibilidad en el abdomen
        - Latido rapido del corazón
        - Diarrea
        - Adelgazamiento""")
sintoma_enfermedad[16]=("""
        - Heces Grasos y malolientes
        - Ictericia""")

#Hepatitis
sintoma_enfermedad[17]=("""
        - Fatiga
        - Nauseas y vomitos
        - Escasa fiebre""")
sintoma_enfermedad[18]=("""
        - Perdida de apetito
        - Malestar abdominal
        - Perdida de apetito
        - Dolor articular""")
sintoma_enfermedad[19]=("""
        - Orina de color oscuro
        - Dolor en la zona del higado
        - Evacuaciones intestinales de color arcilla""")
    
#
sintoma_enfermedad[20]=("""
        - Dificultad para respirar 
        - Dolor en el pecho 
        - Dolores de cabeza""")
sintoma_enfermedad[21]=("""
        - Fatiga
        - Debilidad 
        - Manos y pies fríos""")
sintoma_enfermedad[22]=("""
        - Piel pálida o amarillenta
        - Latidos del corazón irregulares
        - Mareos o aturdimiento""")

#
sintoma_enfermedad[23]=("""
        - Dolor en el hombro derecho  
        - Dolor de espalda justo entre las escápulas""")

sintoma_enfermedad[24]=("""
        - Dolor en la parte superior derecho del abdomen
        - Dolor repentino en la parte central del abdomen""")
sintoma_enfermedad[25]=("""
        - Nauseas y vomito""")




imagen_boton=(ImageTk.PhotoImage(Image.open("Covid2.jpg")))
imagen_boton2=(ImageTk.PhotoImage(Image.open("gastritis2.jpg")))
imagen_boton3=(ImageTk.PhotoImage(Image.open("tuberculosis-3.jpg")))
imagen_boton4=(ImageTk.PhotoImage(Image.open("insuficiencia renal-4.jpg")))
imagen_boton5=(ImageTk.PhotoImage(Image.open("diabetes2.jpg")))
imagen_boton6=(ImageTk.PhotoImage(Image.open("Hipertensión2.jpg")))
imagen_boton7=(ImageTk.PhotoImage(Image.open("Pancreatitis2.jpg")))
imagen_boton8=(ImageTk.PhotoImage(Image.open("Hepatitis2.jpg")))
imagen_boton9=(ImageTk.PhotoImage(Image.open("anemia2.jpg")))
imagen_boton10=(ImageTk.PhotoImage(Image.open("calculos2.jpg")))

Label(raiz, text="Eligir Prueba a Tomar",font="Baskerville 15",bg="light blue",fg="red").place(x=150,y=170)

Button(raiz,text="Covid 19",command=lambda:base.interface(buttonnumber=0,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=40,y=220)   
Label(raiz, image=imagen_boton,height=50,width=60).place(x=35,y=250)



Button(raiz,text="Gastritis",command=lambda:base.interface(buttonnumber=1,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=160,y=220)   
Label(raiz, image=imagen_boton2,height=50,width=60).place(x=155,y=250)

Button(raiz,text="Tuberculosis",command=lambda:base.interface(buttonnumber=2,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=40,y=320)   
Label(raiz, image=imagen_boton3,height=50,width=60).place(x=45,y=350)

Button(raiz,text="Insuficiencia Renal",command=lambda:base.interface(buttonnumber=3,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=140,y=320)   
Label(raiz, image=imagen_boton4,height=50,width=60).place(x=160,y=350)


Button(raiz,text="Diabetes",command=lambda:base.interface(buttonnumber=4,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=280,y=220)
Label(raiz, image=imagen_boton5,height=50,width=60).place(x=275,y=250)


Button(raiz,text="Hipertensión",command=lambda:base.interface(buttonnumber=5,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=400,y=220)
Label(raiz, image=imagen_boton6,height=50,width=60).place(x=405,y=250)

Button(raiz,text="Pancreatitis",command=lambda:base.interface(buttonnumber=6,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=280,y=320)   
Label(raiz, image=imagen_boton7,height=50,width=60).place(x=283,y=350)

Button(raiz,text="Hepatitis",command=lambda:base.interface(buttonnumber=7,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=400,y=320)   
Label(raiz, image=imagen_boton8,height=50,width=60).place(x=396,y=350)


Button(raiz,text="Anemia",command=lambda:base.interface(buttonnumber=8,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=130,y=420)   
Label(raiz, image=imagen_boton9,height=50,width=60).place(x=123,y=450)


Button(raiz,text="Calculos biliares",command=lambda:base.interface(buttonnumber=9,sintoma=sintoma_enfermedad,imagen=imagenes)).place(x=230,y=420) 
Label(raiz, image=imagen_boton10,height=50,width=60).place(x=245,y=450)


consultorio=ImageTk.PhotoImage(Image.open("consultorio.jpg"))
Label(raiz,image=consultorio).pack()

raiz.mainloop()