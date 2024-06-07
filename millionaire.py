Name = input("Enter Your Name: ")
print(f"Welcome {Name}\nWe KBC family welcomes you\nFollowing are the questions for you we hope you will answer it carefully and correctly\nDon't let this opportunity to win money go to waste")


questions = [
   [
      "Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station","longest railway station","None of the above",1
   ],
   [
      "Entomology is the science that studies","Behavior of human beings","Insects","The origin and history of technical and scientific terms","The formation of rocks",2
   ],
   [
      "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of","Asia","Africa","Europe","Australia",2
   ],
   [
      "Garampani sanctuary is located at","Junagarh, Gujarat","Diphu, Assam","Kohima, Nagaland","Gangtok, Sikkim",2
   ],
   [
      "For which of the following disciplines is Nobel Prize awarded?","Physics and Chemistry","Physiology or Medicine","Literature, Peace and Economics","All of the above",4
   ],
   [
      "Hitler party which came into power in 1933 is known as","Labour Party","Nazi Party","Ku-Klux-Klan","Democratic Party",2
   ],
   [
      "FFC stands for","Foreign Finance Corporation","Film Finance Corporation","Federation of Football Council","None of the above",2
   ],
   [
      "Fastest shorthand writer was","Dr. G. D. Bist","J.R.D. Tata","J.M. Tagore","Khudada Khan",1
   ],
   [
      "Epsom (England) is the place associated with","Horse racing","Polo","Shooting","Snooker",1
   ],
   [
      "First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in","1967","1968","1958","1922",1
   ],
   [
      "Galileo was an Italian astronomer who","developed the telescope","discovered four satellites of Jupiter","discovered that the movement of pendulum produces a regular time measurement","All of the above",4
   ],
   [
      "Exposure to sunlight helps a person improve his health because","the infrared light kills bacteria in the body","resistance power increases","the pigment cells in the skin get stimulated and produce a healthy tan","the ultraviolet rays convert skin oil into Vitamin D",4
   ],
   [
      "Golf player Vijay Singh belongs to which country?","USA","Fiji","India","UK",2
   ],
   [
      "Guarantee to an exporter that the importer of his goods will pay immediately for the goods ordered by him, is known as","Letter of Credit (L/C)","laissezfaire","inflation","None of the above",1
   ],
   [
      "First Afghan War took place in","1839","1843","1833","1848",1  
   ],
   [
      "First China War was fought between","China and Britain","China and France","China and Egypt","China and Greek",1
   ],
   [
      "For the Olympics and World Tournaments, the dimensions of basketball court are","26 m x 14 m","28 m x 15 m","27 m x 16 m","28 m x 16 m",2
   ]
]


price = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000)
money = 0
for i in range(0,len(questions)):
   question = questions[i]
   print(f"\n\nquestion for Rs. {price[i]}")
   print(f"{question[0]}")
   # a=question[1]
   # b=question[2]
   # c=question[3]
   # d=question[4]
   print(f"1) {question[1]}     2) {question[2]}")
   print(f"3) {question[3]}       4) {question[4]}")
   reply = int(input("Enter your ans or type (5)quit: "))
   if (reply == 5):
     money = price[i-1]
     break
   if reply == question[-1]:
      print(f"Congratulation you have won {price[i]}")
      if (i==4):
         money = 10000
      elif(i==10):
         money = 320000
      elif(i==16):
         money = 70000000
   else:
      print("Sorry,Try next time")
      break 
print(f"Your Take way Money is {money}")