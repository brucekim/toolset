tmp_cnt=60
target_pid=
target_logfile=$1_ctxt_trend.log
if [ -z "$1" ]
  then
    echo "Usage: $0 process_id "
	exit
fi

target_pid=$1

echo "target pid = $target_pid"
echo "voluntary_ctxt_switches	nonvoluntary_ctxt_switches" 2>&1 | tee -a "$target_logfile"

for ((i=0;i<$tmp_cnt;i++)); do
	grep -E "ctxt" /proc/$target_pid/status | awk '{ print $2 }' | xargs -n2 | tee -a "$target_logfile"
	sleep 1
done
