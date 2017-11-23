# cd 'directory path e.g. D:\test\'
cd 'D:\tmp\gnuplot_cdf'
set terminal png
set output 'cdf_output.png'
set yrange [0:1]
set xrange [0:20000]
set pointsize 0.2
set xlabel "Tput (Kbps)"
set ylabel "CDF"
set title "Throughput A to B" 
set key left top
unset xtics 
set xtics 2000

plot "cdf_cubic_filt.txt" using 1:2 title "TCP cubic" with linespoints,\
 "cdf_htcp_filt.txt" using 1:2 title "TCP htcp" with linespoints,\
 "cdf_highspeed_filt.txt" using 1:2 title "TCP highspeed" with linespoints
 
set output 'out.png'
