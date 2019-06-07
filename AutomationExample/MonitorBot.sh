cvmfs_config probe
cd /home/MonitoringEXOTools/
/home/MonitoringEXOTools/GetToken.py
/home/MonitoringEXOTools/EXO-CMS-MC-JRTracker/Cookies.sh
/home/MonitoringEXOTools/EXO-CMS-MC-JRTracker/TrackingRequestsMain.py
scp -r /home/MonitoringEXOTools/HTML/EXO_MC_Monitoring jruizalv@lxplus.cern.ch:~/www/
mv /home/MonitoringEXOTools/*.csv /home/MonitoringEXOTools/MonitoringData/
