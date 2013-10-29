set term png size 1280,360
set output "ex10_FCFS.png"
unset key

#maximum value somehow
set xrange [0:641]
set yrange [0:1]
set xtics 0
set ytics 0
set xtics rotate by -45
set xtics add ("0" 0) 
set xtics add ("135" 135)
set xtics add ("145" 145)
set xtics add ("247" 247)
set xtics add ("303" 303)
set xtics add ("368" 368)
set xtics add ("516" 516)
set xtics add ("641" 641)


#rectrangles are startx,starty to finishx,finishy
set obj rect from 0, 0 to 135, 1 lw 1.0 fc  rgb "red" 
set obj rect from 145, 0 to 247, 1 lw 1.0 fc  rgb "green" 
set obj rect from 247, 0 to 303, 1 lw 1.0 fc  rgb "blue"
set obj rect from 303, 0 to 368, 1 lw 1.0 fc  rgb "brown" 
set obj rect from 368, 0 to 516, 1 lw 1.0 fc  rgb "yellow" 
set obj rect from 516, 0 to 641, 1 lw 1.0 fc  rgb "violet" 

#lebals take the center as coordinates
#decrementing 5 is so that the lables are moer or less venterev
set style fill pattern 2 border 1
set label font ",20" at 67.5-5,.5 "P1"
set label font ",20" at 195-5,.5 "P2"
set label font ",20" at 275-5,.5 "P3"
set label font ",20" at 325,.5 "P6"
set label font ",20" at 430,.5 "P4"
set label font ",20" at 565,.5 "P5"

plot -1 
