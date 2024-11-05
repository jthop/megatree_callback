




<!-- last div intentionally skipped to fix footer background -->




<?php

if (isset($_POST["ReinstallScript"]))
{
$outputReinstallScript = shell_exec(escapeshellcmd("sudo ".$pluginDirectory."/".$_GET['plugin']."/scripts/fpp_install.sh"));
}

$store = array(
    'dev_server' => '10.10.2.50',
    'prod_server' => 'megatr.ee',
    'mode' => 'dev',
);

$fp = fopen('config.txt','w');

fwrite($fp,serialize($store));


// Reading the data
$infotxt = file_get_contents('info.txt');
$info = unserialize($infotxt);


// Now you can access those normally like arrays:
echo $info['dev_server'];
echo $info['prod_server'];
echo $info['mode'];

?>

<div id="megatree_callback" class="settings">
<fieldset>
<legend>megatr.ee callback plugin</legend>

<form action="plugin_setup.php" method="GET">
Dev Server: <input type="text" name="dev"><br>
Prod Server: <input type="text" name="prod"><br>
Mode: <input type="text" name="mode"><br>

<input type="submit">
</form>

