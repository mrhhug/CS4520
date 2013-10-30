set term png size 1280,420
set output "ex13_SRT.png"
unset key
set title "Michael Hug Assignment 4 ex13_SRT\nP1=135 ; P2=102 ; P3=56 ; P4=148 ; P5=125; P6=65\n"

#xtics - job changes
set xrange [0:641]
set yrange [0:1]
set xtics 0
set ytics 0
set xtics rotate by -45
set xtics add ("0 : P1 start" 0) 
set xtics add ("135 : P1 end" 135)
set xtics add ("145 : P3 start" 145)
set xtics add ("247 : P2 end; P3 start" 247)
set xtics add ("303 : P3 end; P6 Start" 303)
set xtics add ("368 : P6 end; P4 Start" 368)
set xtics add ("516 : P4 end; P5 Start" 516)
set xtics add ("641 : P5 end" 641)

#incomming jobs
set x2tics ("641 : sim over" 641)
set x2tics rotate by 45
set x2tics add ("0 : P1 arrival" 0)
set x2tics add ("145 : P2 arrival" 145)
set x2tics add ("200 : P3,P6 arrival" 200)
set x2tics add ("300 : P4 arrival" 300)
set x2tics add ("400 : P5 arrival" 400)

#rectrangles are startx,starty to finishx,finishy
set obj rect from 0, 0 to 135, 1 lw 1.0 fc  rgb "red" 
set obj rect from 145, 0 to 247, 1 lw 1.0 fc  rgb "green" 
set obj rect from 247, 0 to 303, 1 lw 1.0 fc  rgb "blue"
set obj rect from 303, 0 to 368, 1 lw 1.0 fc  rgb "brown" 
set obj rect from 368, 0 to 516, 1 lw 1.0 fc  rgb "yellow" 
set obj rect from 516, 0 to 641, 1 lw 1.0 fc  rgb "violet" 

#labels
set style fill pattern 2 border 1
set label font ",20" at 67.5-5,.5 "P1"
set label font ",20" at 195-5,.5 "P2"
set label font ",20" at 275-5,.5 "P3"
set label font ",20" at 325,.5 "P6"
set label font ",20" at 430,.5 "P4"
set label font ",20" at 565,.5 "P5"

plot -1 
