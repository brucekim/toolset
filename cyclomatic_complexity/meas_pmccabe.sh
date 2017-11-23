find ./ -name *.cpp -o -name *.c -o -name *.h | xargs ./tools/pmccabe | sort -nr 2>&1 | tee complexity.log
