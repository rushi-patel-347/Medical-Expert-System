from experta import *

#FactEngine class 
class FactEngine(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print("Hi! I'm here to help you.")
		print("You will be required to answer a few questions about your medical conditions in order to improve your health.")
		print("Are you suffering from any of the following symptoms:")
		print("")
		yield Fact(action="check_disease")

	@Rule(Fact(action='check_disease'), NOT(Fact(back_pain=W())),salience = 1)
	def input_symptom_0(self):
		self.declare(Fact(back_pain=input("Back Pain: ").strip().lower()))

	@Rule(Fact(action='check_disease'), NOT(Fact(cough=W())),salience = 1)
	def input_symptom_1(self):
		self.declare(Fact(cough=input("Cough: ").strip().lower()))

	@Rule(Fact(action='check_disease'), NOT(Fact(headache=W())),salience = 1)
	def input_symptom_2(self):
		self.declare(Fact(headache=input("Headache: ").strip().lower()))

	@Rule(Fact(action='check_disease'), NOT(Fact(fainting=W())),salience = 1)
	def input_symptom_3(self):
		self.declare(Fact(fainting=input("Fainting: ").strip().lower()))

	@Rule(Fact(action='check_disease'), NOT(Fact(fatigue=W())),salience = 1)
	def input_symptom_4(self):
		self.declare(Fact(fatigue=input("Fatigue: ").strip().lower()))
	 
	@Rule(Fact(action='check_disease'), NOT(Fact(low_body_temp=W())),salience = 1)
	def input_symptom_5(self):
		self.declare(Fact(low_body_temp=input("Low Body Temperature: ").strip().lower()))
	
	@Rule(Fact(action='check_disease'), NOT(Fact(sore_throat=W())),salience = 1)
	def input_symptom_6(self):
		self.declare(Fact(sore_throat=input("Sore Throat: ").strip().lower()))
	
	@Rule(Fact(action='check_disease'), NOT(Fact(chest_pain=W())),salience = 1)
	def input_symptom_7(self):
		self.declare(Fact(chest_pain=input("Chest Pain: ").strip().lower()))
	
	@Rule(Fact(action='check_disease'), NOT(Fact(restlessness=W())),salience = 1)
	def input_symptom_8(self):
		self.declare(Fact(restlessness=input("Restlessness: ").strip().lower()))
	
	@Rule(Fact(action='check_disease'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def input_symptom_9(self):
		self.declare(Fact(sunken_eyes=input("Sunken Eyes: ").strip().lower()))
	
	@Rule(Fact(action='check_disease'), NOT(Fact(nausea=W())),salience = 1)
	def input_symptom_10(self):
		self.declare(Fact(nausea=input("Nausea: ").strip().lower()))

	@Rule(Fact(action='check_disease'), NOT(Fact(fever=W())),salience = 1)
	def input_symptom_11(self):
		self.declare(Fact(fever=input("Fever: ").strip().lower()))
	
	@Rule(Fact(action='check_disease'), NOT(Fact(blurred_vision=W())),salience = 1)
	def input_symptom_12(self):
		self.declare(Fact(blurred_vision=input("Blurred Vision: ").strip().lower()))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Alzheimers"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_1(self):
		self.declare(Fact(disease="Arthritis"))
		
	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_2(self):
		self.declare(Fact(disease="Asthma"))
				
	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_3(self):
		self.declare(Fact(disease="Babesiosis"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_4(self):
		self.declare(Fact(disease="Bronchiectasis"))
				
	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_5(self):
		self.declare(Fact(disease="Celiac"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_6(self):
		self.declare(Fact(disease="Chest Infection"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_7(self):
		self.declare(Fact(disease="Chikungunya"))
		
	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_8(self):
		self.declare(Fact(disease="Chlamydia"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_9(self):
		self.declare(Fact(disease="Cholera"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_10(self):
		self.declare(Fact(disease="Chronic Kidney Disease"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="yes"))
	def disease_11(self):
		self.declare(Fact(disease="Conjunctivitis Pink Eye"))
			
	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_12(self):
		self.declare(Fact(disease="Crabs"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_13(self):
		self.declare(Fact(disease="Dengue"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_14(self):
		self.declare(Fact(disease="Diabetes"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_15(self):
		self.declare(Fact(disease="Epilepsy"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_16(self):
		self.declare(Fact(disease="Gastroenteritis"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_17(self):
		self.declare(Fact(disease="Glaucoma"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_18(self):
		self.declare(Fact(disease="Heart Disease"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_19(self):
		self.declare(Fact(disease="Heat Stroke"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_20(self):
		self.declare(Fact(disease="Hemophilia"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_21(self):
		self.declare(Fact(disease="Hyperthyroidism"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_22(self):
		self.declare(Fact(disease="Hypothermia"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="yes"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_23(self):
		self.declare(Fact(disease="Insomnia"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_24(self):
		self.declare(Fact(disease="Jaundice"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_25(self):
		self.declare(Fact(disease="Kidney_Stones"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_26(self):
		self.declare(Fact(disease="Liver_Cancer"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_27(self):
		self.declare(Fact(disease="Lymphoma"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_28(self):
		self.declare(Fact(disease="Malaria"))
	
	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_29(self):
		self.declare(Fact(disease="Measles"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="yes"))
	def disease_30(self):
		self.declare(Fact(disease="Ovarian cancer"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_31(self):
		self.declare(Fact(disease="Pedal edema"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_32(self):
		self.declare(Fact(disease="Pleurisy"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_34(self):
		self.declare(Fact(disease="Sepsis"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="yes"))
	def disease_35(self):
		self.declare(Fact(disease="Sickle Cell Disease"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_36(self):
		self.declare(Fact(disease="Sinusitis"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="yes"))
	def disease_37(self):
		self.declare(Fact(disease="Stroke"))

	@Rule(Fact(action='check_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_38(self):
		self.declare(Fact(disease="Tuberculosis"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_39(self):
		self.declare(Fact(disease="Vertigo"))

	@Rule(Fact(action='check_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_40(self):
		self.declare(Fact(disease="Yellow fever"))

	@Rule(Fact(action='check_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		print("==========================================================> \n")
		disease_details = get_disease_description(disease)
		treatments = get_disease_treatments(disease)
		print("==========================================================> \n")
		print("You are most likely suffering from %s\n" %(disease))
		print("==========================================================> \n")
		print("A brief explanation of the disease is provided below:\n")
		print(disease_details+"\n")
		print("==========================================================> \n")
		print("Common medication and procedures recommendations are as follows:: \n")
		print(treatments+"\n")



	@Rule(Fact(action='check_disease'),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(cough=MATCH.cough),
		  Fact(headache=MATCH.headache),
		  Fact(fainting=MATCH.fainting),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(fever=MATCH.fever),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		print("\nThere is no disease that matched your specific symptoms.")
		lis = [ back_pain, cough, headache, fainting, fatigue, low_body_temp, sore_throat, chest_pain, restlessness, sunken_eyes ,nausea,fever, blurred_vision]
		lis = lis.sort()
		max_count = 0
		no_of_disease = ""
		try:
			for key,val in diseases_symptom_dic.items():
				count = 0
				temp_list = eval(key)
				for j in range(0,len(lis)):
					if(temp_list[j] == lis[j] and lis[j] == "yes"):
						count = count + 1
				if count > max_count:
					max_count = count
					no_of_disease = val
			not_found(no_of_disease)
		except:
			print("\nPlease add symptom answers as yes or no only.\n")

diseases_name_list = []
diseases_signs = []
diseases_symptom_dic = {}
diseases_desc_dic = {}
diseases_treatment_dic = {}

# loads the disease files
def load_data():
	global diseases_name_list,diseases_signs,diseases_symptom_dic,diseases_desc_dic,diseases_treatment_dic
	diseases = open("diseases.txt")
	diseases_names = diseases.read()
	diseases_name_list = diseases_names.split("\n")
	diseases.close()
	for disease in diseases_name_list:
		disease = disease.strip()
		# load disease symptoms data
		disease_sympton_file = open("Disease symptoms/" + disease + ".txt")
		disease_sympton_data = disease_sympton_file.read()
		s_list = disease_sympton_data.split("\n")
		diseases_signs.append(s_list)
		diseases_symptom_dic[str(s_list)] = disease
		disease_sympton_file.close()
		# load disease description data
		disease_desc_file = open("Disease descriptions/" + disease + ".txt")
		disease_desc_data = disease_desc_file.read()
		diseases_desc_dic[disease] = disease_desc_data
		disease_desc_file.close()
		# load disease treatment data
		disease_tert_file = open("Disease treatments/" + disease + ".txt")
		disease_tert_data = disease_tert_file.read()
		diseases_treatment_dic[disease] = disease_tert_data
		disease_tert_file.close()
	
# get the disease description as per the paramter
def get_disease_description(disease):
	return diseases_desc_dic[disease]

# get the disease treatment as per the paramter
def get_disease_treatments(disease):
	return diseases_treatment_dic[disease]

# shows the details for the predicted disease if none of the facts matched
def not_found(disease):
	print("==========================================================> \n")
	disease_detail = get_disease_description(disease)
	disease_treatments = get_disease_treatments(disease)
	print("")
	print("==========================================================> \n")
	print("You are most likely suffering from %s\n" %(disease))
	print("==========================================================> \n")
	print("Below is a brief description of the disease:\n")
	print(disease_detail+"\n")
	print("==========================================================> \n")
	print("Other real doctors' common medications and procedures are as follows: \n")
	print(disease_treatments+"\n")


if __name__ == "__main__":
	load_data()
	f_engine = FactEngine()
	while(1):
		f_engine.reset()  # Initalizing the engine.
		f_engine.run()  # start the engine.
		print("Do you want to diagnose any additional symptoms?")
		if input().lower() == "no":
			exit()
