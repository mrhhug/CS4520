set term png size 1280,360
set output "ex8_RR.png"
unset key

#maximum value somehow
set xrange [0:576]
set yrange [0:1]
set xtics 0
set ytics 0
set x2tics 576
set xtics rotate by -45
set xtics add ("0" 0)
set xtics add ("135" 135)
set xtics add ("145" 145)
set xtics add ("195" 195)
set xtics add ("245" 245)
set xtics add ("295" 295)
set x2tics add ("297" 297)
set xtics add ("303" 303)
set xtics add ("353" 353)
set xtics add ("403" 403)
set xtics add ("453" 453)
set xtics add ("501" 501)
set xtics add ("576" 576)

#rectrangles are startx,starty to finishx,finishy
set obj rect from 0, 0 to 135, 1 lw 1.0 fc  rgb "red" 
set obj rect from 145, 0 to 245, 1 lw 1.0 fc  rgb "green" 
set obj rect from 245, 0 to 295, 1 lw 1.0 fc  rgb "blue"
set obj rect from 295, 0 to 297, 1 lw 1.0 fc  rgb "green"
set obj rect from 297, 0 to 303, 1 lw 1.0 fc  rgb "blue"
set obj rect from 303, 0 to 403, 1 lw 1.0 fc  rgb "yellow" 
set obj rect from 403, 0 to 453, 1 lw 1.0 fc  rgb "violet"
set obj rect from 453, 0 to 501, 1 lw 1.0 fc  rgb "yellow"
set obj rect from 501, 0 to 576, 1 lw 1.0 fc  rgb "violet"

#lebals take the center as coordinates
#decrementing 5 is so that the lables are moer or less venterev
#set style fill pattern 2 border 1
set label font ",20" at 67.5-5,.5 "P1"
set label font ",20" at 195-5,.5 "P2"
set label font ",20" at 265,.5 "P3"
set label font ",20" at 345,.5 "P4"
set label font ",20" at 420,.5 "P5"

plot -1 
