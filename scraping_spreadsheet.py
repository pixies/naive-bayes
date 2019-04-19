from pyexcel_ods3 import get_data
import os

def get_files(path): 
    """	
		return a list with all files for scraping
    """
    for p, _, files in os.walk(os.path.abspath(path)): 
   		return files[1:][::-1]

def get_planilha(file):
	"""
		return a list with all desired values of one spreadshet
	"""
	planilha = get_data(file, start_columm=3, columm_limit=2)
	planilha = planilha['CÁLCULOS']

	local_amostra = planilha[2][-1]
	values = []
	values.append(planilha[3][-1])
	values.append(planilha[5][-1])
	values.append(planilha[11][-1])
	values.append(planilha[13][-1])
	values.append(planilha[15][-1])
	values.append(planilha[17][-1])
	values.append(planilha[20][-1])
	values.append(planilha[21][-1])
	if planilha[24][-1] == 'Branda':
		values.append(1)
	elif planilha[24][-1] == 'Moderada':
		values.append(2)
	elif planilha[24][-1] == 'Dura':
		values.append(3)
	elif planilha[24][-1] == 'Muito dura':
		values.append(4)
	values.append(local_amostra)
		
	return values

def convert_list_str(lista):
	s = ''
	for item in lista:
		s += str(item)
		s += ", "
		s = s[:-1]
	return s

def main():
	path = "files/"
	files = get_files(path)
	print("Arquivos encontrados no diretório: ", get_files(path))
	f = open('tmp/test.csv', "w+")
	for file in files:
		f.write(convert_list_str(get_planilha(path+file))[:-1] + "\n")
		print(convert_list_str(get_planilha(path+file))[:-1])
	f.close()



if __name__ == '__main__':
	main()