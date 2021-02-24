# tp_ros_ialy


Mon package contient deux noeuds ( publisher et subscriber)

Et que le but de ce projet est de suivre la trajectoire d ' un huit ( visualiser sur rviz ) en utilisant posStamped a 15hz

# Installation

Pour installer ce noeud il faut le cloner dans le dossier src de votre catkin workspace (catkin_ws)

commande a suivre:

"""

 	cd catkin_ws/src
 	
 	git clone https://github.com/ialy/tp_ros_ialy.git
 	
 	catkin build
 	
	cd ..
	
	source devel/setup.bash
	
"""

# compilation

afin de compiler les noeuds, on peut proceder avec:
	
	
 ## rosrun
 
 
 
 --- 1er terminal ---
 
 lancement du serve
 
 """
 
	Ouvrez un premier terminal: 'ctrl + alt + t ' 

	lancer le roscore: 'roscore'

"""




 --- 2e terminal ---
 
 execution du publisher
 
 """

	 Ouvrez un autre  terminal: 'ctrl + alt + t ' 
 
	 aller dans le dossier catkin_ws: 'cd catkin_ws'

	 sourcer: ' sourcer le devel/setup.bash'
	 
 	 executer: 'rosrun tp_ros_ialy pub.py'

"""




 --- 3e terminal ---
 
  execution du subcriber ou lire les topic publier 
 
"""
 
 	Ouvrez un autre  terminal: 'ctrl + alt + t ' 
  
	aller dans le dossier catkin_ws: 'cd catkin_ws'
  
	sourcer: ' sourcer le devel/setup.bash'
	
"""
 
 
 *** 1er cas ***

"""

	executer: 'rosrun tp_ros_ialy sub.py'

"""


 ----- NB 

en cas de probleme sur le 3e terminal, il y une non-correspondance sur le topic( utilisation de remap)

"""

dans le "3e terminal": 'rosrun tp_ros_ialy sub.py topic_sub:=topic_pub'

"""


  *** 2e cas ***
 
"""

	executer: 'rostopic echo /topic_pub'

"""



 --- 4e terminal ----
 
 
  lancement du rviz
 
 """
 
	Ouvrez un autre  terminal: 'ctrl + alt + t ' 
 
	aller dans le dossier catkin_ws: 'cd catkin_ws'
 
	sourcer: ' sourcer le devel/setup.bash'
 
	executer : ' rosrun rviz rviz '
  
	clicker sur : "add" -> "by topic" ->  'pose'(sur /topic_pub) -> ok
  
 """ 
  
  en resultat, vous voyer le pose fait un trajectoire d un huit (8)
  
 
 
 
 
 
 ## roslaunch

Afin de resumer l execution sur le 'rosrun', le roslauch peut facilite  la tache 

"""

  	Ouvrez un autre  terminal: 'ctrl + alt + t ' 
  
 	aller dans le dossier catkin_ws: 'cd catkin_ws'
  
	sourcer: ' sourcer le devel/setup.bash'

	executer : ' roslaunch tp_ros_ialy ialy.launch'

"""

  en resultat, vous voyer le pose fait un trajectoire d un huit ( la meme que l execution sur le rosrun )
  
  
