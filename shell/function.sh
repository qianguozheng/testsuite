# Reference from :http://www.ibm.com/developerworks/cn/linux/l-cn-shell-monitoring/
#monitor the process
function GetPID #User #Name
{
	PsUser=$1
	PsName=$2
	pid=`ps -u $PsUser| grep $PsName| grep -v grep| grep -v vi| grep -v dbx\n| grep -v tail| grep -v stat| grep -v stop| sed -n 1p | awk '{print $1}'`
	echo $pid
}

#PID=`GetPID weeds sshd`
#
#if [ "-$PID" == "-" ]
#then
#{
#	echo "The Process does not exist"
#}
#fi
#echo $PID

# Get CPU usage of percentage, ps not like top, need figure out the difference.
function GetCpu
{
	CpuValue=`ps -p $1 -o pcpu| grep -v CPU | awk '{print $1}' | awk -F. '{print $1}'`
	echo $CpuValue
}

function CheckCpu
{
	PID=$1
	cpu=`GetCpu $PID`
	if [ $cpu -gt 80 ]
	then
	{
		echo "The usage of cpu is larger than 80%"
	}
	else
	{
		echo "The usage of cpu is normal : $cpu"
	}
	fi
}

cpusg=`CheckCpu 3043`
echo "CPU Usage: $cpusg"

#monitor the memory usage of process
function GetMem
{
	MEMUsage=`ps -o vsz -p $1| grep -v VSZ`
	((MEMUsage/=1000))
	echo $MEMUsage
}
mem=`GetMem 3043`
echo "Memory Usage: $mem"

# Get the file descriptor
function GetDes
{
	DES=`ls /proc/$1/fd | wc -l`
	echo $DES
}

des=`GetDes 3043`
echo "File Descriptor: $des"

function Listening
{
	TCPListeningnum=`netstat -an | grep ":$1 " |  awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l`
	UDPListeningnum=`netstat -an| grep ":$1 "  | awk '$1 == "udp" && $NF == "0.0.0.0:*" {print $0}' | wc -l`
	(( Listeningnum = TCPListeningnum + UDPListeningnum ))
	if [ $Listeningnum == 0 ]
	then
	{
		echo "0"
	}
	else
	{
		echo "0"
	}
	fi
}

isListen=`Listening 8080`
echo "isListen=$isListen"

# get the process run num
function Runnum #process name
{
	runnum=`ps -ef | grep -v vi | grep -v tail | grep "$1" | grep -v grep | wc -l`
	echo $runnum
}
run=`Runnum sshd`
echo $run

function GetSysCPU
{
CpuIdle=`vmstat 1 5 | sed -n '3,$p' | awk '{x = x + $15} END {print x/5}' | awk -F. '{print $1}'`
CpuNum=`echo "100-$CpuIdle" | bc`
echo $CpuNum
}

echo "CPU Load=`GetSysCPU`%"

function GetDiskSpc
{
	if [ $# -ne 1 ]
	then
		return 1
	fi
	Folder="$1$"
	DiskSpace=`df -k| grep $Folder | awk '{print $5}' | awk -F% '{print $1}'`
	echo $DiskSpace
}
echo "Disk Space: `GetDiskSpc /`%"
