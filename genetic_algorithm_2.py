import random
#GENETİK ALGORİTMA İLE DİZE OLUŞTURMA 
# Her nesildeki birey sayısı
POPULATION_SIZE = 100

# Geçerli genler
GENES = '''abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

# Oluşturulacak hedef kromozom
TARGET = "Fırat Üni Adli Bilişim Mühendisliği Barış Ceviz"

#Popülasyondaki bireyi temsil eden sınıfı oluşturduk
class Person(object):	
	
	def __init__(self, chromosome):
		self.chromosome = chromosome
		self.fitness = self.cal_fitness()

	@classmethod
	def mutated_genes(self):
		#Mutasyan için rastgele genler oluşturulacak
		global GENES
		gene = random.choice(GENES)
		return gene

	@classmethod
	def create_gnome(self):
		#Kromozom veya gen değeri oluşturacağız
		global TARGET
		gnome_len = len(TARGET)
		return [self.mutated_genes() for _ in range(gnome_len)]

	def partner(self, par2):
		#Çiftleştirme işlemi uygulanıp çocuk elde edilecek

		#Çocuklar için kromozom oluşturacağız
		child_chromosome = []
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):
			#genparent1,gp2 == ebeveyn1 ve ebeveyn2 Rastgele olsalık değeri
			prob = random.random()

			# Prob değerimiz 0.45'ten küçükse gp1'den gen ekleyin
			if prob < 0.45:
				child_chromosome.append(gp1)

			# Prob değerimiz 0.45'ten büyük 0.90'dan küçükse gp2'den gen ekleyin
			elif prob < 0.90:
				child_chromosome.append(gp2)

			# Bunların hiçbiri olmazsa mutasyonlu gen ekle. Bu işlemin yapılma sebebi çeşitliliği korumak
			else:
				child_chromosome.append(self.mutated_genes())

		# Çocuklar için oluşturduğumuz kromozomu(child_chromosome) kullanarak yeni bir birey(person) oluşturuyoruz
		return Person(child_chromosome)

	def cal_fitness(self):
		# Fitness değerini hesaplayacağımız fonks. kromozom target değerimize benzemiyorsa fitness değerini 1 arttıracağız
		global TARGET
		fitness = 0
		for gs, gt in zip(self.chromosome, TARGET):
			if gs != gt: fitness+= 1
		return fitness

# Kodun çalıştırdığımız fonks. oluşturuyoruz.
def main():

	global POPULATION_SIZE
	#Jenerasyonu 
	generation = 1
	found = False
	population = []
	# Popülasyonumuza genimizi ekleyeceğiz
	for _ in range(POPULATION_SIZE):
				gnome = Person.create_gnome()
				population.append(Person(gnome))

	while not found:
		#Popülasyonu en yüksek fitness puanına sahip olandan başlat
		population = sorted(population, key = lambda x:x.fitness)

		# Oluşturduğumuz kromozomların fitness değeri 0'a eşitse o zaman biz en iyi geni bulduğumuz için döngüyü bitiriyoruz.
		if population[0].fitness <= 0:
			found = True
			break

		# fitness değeri 0 değilse yeni genler(çocuklar) üretiyoruz. 
		new_generation = []

		# Popülasyondan yani en iyi nufüsun %10 luk kısmına alıp yeni jenerasyona ekliyoruz
		s = int((10*POPULATION_SIZE)/100)
		new_generation.extend(population[:s])

		# Popülasyonun kalanını yeni bireyler(kromozomlar) için çiftleştirip yeni jenerasyona ekliyoruz.
		s = int((90*POPULATION_SIZE)/100)
		for _ in range(s):
			parent1 = random.choice(population[:50])
			parent2 = random.choice(population[:50])
			child = parent1.partner(parent2)
			new_generation.append(child)

		population = new_generation

		print("\tJenerasyon: {}\t\tDeğer: {}\t\tUygunluk: {}".\
			format(generation,
			"".join(population[0].chromosome),
			population[0].fitness))

		generation += 1

	print("\tJenerasyon: {}\t\tDeğer: {}\t\tUygunluk: {}".\
		format(generation,
		"".join(population[0].chromosome),
		population[0].fitness))

if __name__ == '__main__':
	main()