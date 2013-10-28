set term png size 1280,360
set output "ex7_SPN.png"
unset key

#maximum value somehow
set xrange [0:576]
set yrange [0:1]
set xtics 0
set ytics 0
set xtics rotate by -45
set xtics add ("0" 0) 
set xtics add ("135" 135)
set xtics add ("145" 145)
set xtics add ("247" 247)
set xtics add ("303" 303)
set xtics add ("451" 451)
set xtics add ("576" 576)


#rectrangles are startx,starty to finishx,finishy
set obj rect from 0, 0 to 135, 1 lw 1.0 fc  rgb "red" 
set obj rect from 145, 0 to 247, 1 lw 1.0 fc  rgb "green" 
set obj rect from 247, 0 to 303, 1 lw 1.0 fc  rgb "blue" 
set obj rect from 303, 0 to 451, 1 lw 1.0 fc  rgb "yellow" 
set obj rect from 451, 0 to 576, 1 lw 1.0 fc  rgb "violet" 

#lebals take the center as coordinates
#decrementing 5 is so that the lables are moer or less venterev
set style fill pattern 2 border 1
set label font ",20" at 67.5-5,.5 "P1"
set label font ",20" at 195-5,.5 "P2"
set label font ",20" at 275-5,.5 "P3"
set label font ",20" at 377-5,.5 "P4"
set label font ",20" at 513.5-5,.5 "P5"

plot -1 
