<?php
if($_SERVER['REQUEST_METHOD'] == "POST") {
	$command = '/usr/bin/python3 /var/www/stads.mathiaspihl.com/main.py '.escapeshellarg($_POST['user']).' '.escapeshellarg($_POST['pass']);
	//$command = 'echo "test"';
	//echo $command;
	echo exec($command);
} else {
echo "Use by POSTing 'user' and 'pass' as form-data and wait a short 35 seconds for an answer.... #throttling"; 
}
