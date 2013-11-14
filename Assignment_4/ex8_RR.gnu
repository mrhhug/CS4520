set term png size 1280,420
set output "ex8_RR.png"
unset key
set title "Michael Hug Assignment 4 ex8_RR\nP1=135 ; P2=102 ; P3=56 ; P4=148 ; P5=125;\n\n297 : P2 end; P3 resume"

#xtics - job changes
set xrange [0:576]
set yrange [0:1]
set xtics 0
set ytics 0
set x2tics 576
set xtics rotate by -45
set xtics add ("0 : P1 start" 0)
set xtics add ("50 : RR check" 50)
set xtics add ("100 : RR check" 100) 
set xtics add ("135 : P1 end" 135)
set xtics add ("145 : P2 start" 145)
set xtics add ("195 : RR check" 195)
set xtics add ("245 : P2 stop; P3 start" 245)
set xtics add ("295 : P3 stop; P2 resume" 295)
set xtics add ("303 : P3 end; P4 start" 303)
set xtics add ("353 : RR check" 353)
set xtics add ("403 : P4 stop; P5 start" 403)
set xtics add ("453 : P5 stop; P4 resume" 453)
set xtics add ("501 : P4 end; P5 resume" 501)
set xtics add ("551 : RR check" 551)
set xtics add ("576 : P5 end" 576)

#incomming jobs
set x2tics ("576 : sim over" 576)
set x2tics rotate by 45
set x2tics add ("0 : P1 arrival" 0)
set x2tics add ("145 : P2 arrival" 145)
set x2tics add ("200 : P3 arrival" 200)
set x2tics add ("300 : P4 arrival" 300)
set x2tics add ("400 : P5 arrival" 400)

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

plot (0,297)
