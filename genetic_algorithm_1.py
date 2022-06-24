import random

class Genetic:
    def __init__(self, Target, Population_Number):
        self.Gene_Pool = '''abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHİIJKLMNOÖPQRŞSTUÜVWXYZ 1234567890,.-;:_!"#%&/()=?@${[]}'''
        self.Target = Target #Hedef bireyimizin geni
        self.Population_Number = Population_Number #Popülasyondaki birey sayısı
        self.Target_Text_Lenght = len(Target) #Hedef bireyimizin uzunluğu
        self.Population = [] #Popülasyondaki bireylerin bulunacağı dizi
        self.Next_Generation = [] #Yeni nesildeki bireylerin bulunacağı dizi
        self.Found = False #Hedef bireyi bulup bulmadığımızı gösteren
        self.Generation_Timer = 0 #Kaç nesil ilerlediğimizi gösterir

    class Member: #Bireylerin tanımlandığı fonksiyon
        def __init__(self,chromosome):# Kromozom = Birey
            self.Chromosome = chromosome 
            self.Fitness = 0 #Başlangıç değeri olarak fitness değeri 0 tanımlandı

    def random_gene(self): #İlk bireyleri oluşturmak için rastgele gen oluşturma fonksiyonu
        Gene = random.choice(self.Gene_Pool)
        return Gene
	
	#Kromozom oluşturma fonksiyonu
    def create_chromosome(self): #Hedef bireyimizin uzunluğunca kromozom oluşturuldu 
		# Gen oluşturmada "random_gene" fonksiyonu kullanıldı
        chromosome = [self.random_gene() for i in range(self.Target_Text_Lenght)]
        return chromosome

    def calculate_fitness(self): # Bireylerin fitness değerini hesaplamak için fitness fonksiyonu
        for Member in self.Population:
            Member.Fitness = 0 #Fitness değeri 0 dan başladı
            for i in range(self.Target_Text_Lenght): #hedef bireyin uzunluğu kadar döngü sayısı
                if Member.Chromosome[i] == self.Target[i]:
                    #Hedefin indisi mevcut bireyin indisinin değeri ile aynıysa fitness i arttır
                    Member.Fitness += 1

            #Fitness değeri hedef bireyin uzunluğu kadar ise hedef birey bulunmuştur
            if Member.Fitness == self.Target_Text_Lenght:
                self.Found_Text = Member.Chromosome
                self.Found = True #Döngüyü sonlandırmak için Found değeri "True" yapıldı

    def crossover(self): #Çaprazlama işlemi
        #def main() kısmında, çaprazlama işleminden önce popülasyondaki bireyler, fitness değerlerine göre kötüden en iyiye doğru sıralandı
        # Popülasyonun en iyi %10 u alındı (90. indisten sonrası)
        last_best = int(( 90 * self.Population_Number) / 100)

        self.Next_Generation = [] # Yeni jenerasyon oluşturuldu

        #Alınan en iyi %10 luk bireyler yeni jenerasyona aktarıldı
        self.Next_Generation.extend(self.Population[last_best:])

        while True: #Kalan 90 birey, çaprazlama ve mutasyon işlemine sokuldu
            
            #Yeni jenerasyonun uzunluğu Popülasyondaki birey sayısına eşit olana kadar işlemleri gerçekleştir
            if len(self.Next_Generation) < self.Population_Number:
                #En iyi bireylerden biri seçildi ve member_1 e atandı
                member_1 = random.choice(self.Population[last_best:]).Chromosome
                #En iyi bireylerden biri seçildi ve member_2 ye atandı
                member_2 = random.choice(self.Population[last_best:]).Chromosome
                new_member = [] # Çaprazlama sonucu oluşacak birey

                for gene1,gene2 in zip(member_1, member_2):
                    #prob ismide rastgele bir olasılık değeri belirlendi
                    prob = random.random() # 0 - 1

                    if prob < 0.47: #olasılık 0.47 den küçükse 1. ebeveynden gen al
                        new_member.append(gene1)
                    elif prob < 0.95: #olasılık 0.47 den büyük, 0.95 den küçükse 2. ebeveynden gen al
                        new_member.append(gene2)
                    else: #Hiç biri olmazsa mutasyona sok (random gen al)
                        new_member.append(self.random_gene())

                # Oluşturulan bireyi yeni jenerasyon dizisine aktar
                self.Next_Generation.append(self.Member(new_member))
                
            else:
                break

        self.Population = self.Next_Generation #Yeni jenerasyondaki bireyler, artık ana jenerasyonumuz oldu
        print(f"{self.Generation_Timer}. jenerasyon") #Kaç jenerasyon geçtiğini ekrana yazdırır

    # Kodun ana kısmı
    def main(self): 
		#Başlangıç popülasyonunu oluşturmak için for döngüsü açıldı 
        for i in range(self.Population_Number): #Polülasyona birey ekler
            self.Population.append(self.Member(self.create_chromosome()))

        #Founde = TRUE olana kadar (hedef bireye ulaşana kadar) işlemleri tekrarla
        while not self.Found:
            self.calculate_fitness() #Fitness değerini hesapla
            self.Population = sorted(self.Population, key=lambda Member: Member.Fitness) #Popülasyondaki bireyleri sırala
            self.crossover() #Çaprazlama işlemi yap
            self.Generation_Timer += 1 #Nesil numarasını arttır

        print(f"Hedef bireye {self.Generation_Timer}. jenerasyonda ulaşıldı. Hedef = {self.Target}")

Target = input("Hedef Birey: ") #Hedef birey
Population_Number = 100 #Popülasyondaki birey sayısı

#Genetic fonksiyonuna Target ve Population_Number değerleri girildi
Ga = Genetic(Target, Population_Number)
Ga.main()