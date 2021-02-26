# tp_ros_ialy


Mon package contient deux noeuds ( publisher et subscriber)

Et que le but de ce projet est de suivre la trajectoire d' un huit ( visualiser sur rviz ) en utilisant posStamped a 15hz mais avec l interface graphiqye toggle, tu peux l'arreter un appyant

# Installation

Pour installer ce noeud il faut le cloner dans le dossier src de votre catkin workspace (catkin_ws)

commande a suivre:


 	cd catkin_ws/src
 	
 	git clone https://github.com/ialy/tp_ros_ialy.git
 	
 	catkin build
 	
	cd ..
	
	source devel/setup.bash
	

# compilation

afin de compiler les noeuds, on peut proceder avec:
	
	
 ## rosrun
 
 
 
 ### 1er terminal 
 
 lancement du server
 
 
 
	Ouvrez un premier terminal: ctrl + alt + t  

	lancer le roscore: roscore






 ### 2e terminal 
 
 execution du publisher(button gui) et sort un interface graphique toggle
 
 

	 Ouvrez un autre  terminal: ctrl + alt + t 
 
	 aller dans le dossier catkin_ws: cd catkin_ws'

	 sourcer:  source le devel/setup.bash
	 
 	 executer: rosrun tp_ros_ialy button_node.py






 ### 3e terminal 
 
  execution du subcriber(PoseStamped) 
 

 
 	Ouvrez un autre  terminal: ctrl + alt + t  
  
	aller dans le dossier catkin_ws: 'cd catkin_ws'
  
	sourcer:  source le devel/setup.bash

	executer: rosrun tp_ros_ialy PoseStamped




 ----- NB 

en cas de probleme sur le 3e terminal, il y une non-correspondance sur le topic( utilisation de remap)



	dans le "3e terminal": rosrun tp_ros_ialy PoseStampedpy PoseStamped_sub:=button_state




 ### 4e terminal 
 
 
  lancement du rviz
 

 
	Ouvrez un autre  terminal: ctrl + alt + t  
 
	aller dans le dossier catkin_ws: cd catkin_ws
 
	sourcer: source le devel/setup.bash
 
	executer :  rosrun rviz rviz 
  
	clicker sur : "add" -> "by topic" ->  'pose'(sur /tp_note) -> ok
  
  
  
  en resultat, vous voyer le pose fait un trajectoire d un huit (8) et ppeux etre arreter par l inetrface graphique
  
 
 
 
 
 
 ## roslaunch

Afin de resumer l execution sur le 'rosrun', le roslauch peut facilite  la tache 



  	Ouvrez un autre  terminal: ctrl + alt + t  
  
 	aller dans le dossier catkin_ws: cd catkin_ws
  
	sourcer:  source le devel/setup.bash

	executer :  roslaunch tp_ros_ialy tp_ros_ialy.launch



  en resultat, vous voyer le pose fait un trajectoire d un huit ( la meme que l execution sur le rosrun )
  
 
 # astuce
 
 appuyer deux fois sur l interface graphique pour regarder l evolution sur rviz
