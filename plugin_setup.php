<!-- last div intentionally skipped to fix footer background -->
<?php
include_once "/opt/fpp/www/common.php"; //Alows use of FPP Functions
$pluginName = basename(dirname(__FILE__));
$pluginConfigFile = $settings['configDirectory'] ."/plugin." .$pluginName; //gets path to configuration files for plugin
if (file_exists($pluginConfigFile)) {
	$pluginSettings = parse_ini_file($pluginConfigFile);
}

if (strlen(urldecode($pluginSettings['DEV_SERVER']))<1){
	WriteSettingToFile("DEV_SERVER","10.10.2.50",$pluginName);
	$madeChange = true;
}
if (strlen(urldecode($pluginSettings['DEV_SERVER']))<1){
	WriteSettingToFile("PROD_SERVER","megatr.ee",$pluginName);
	$madeChange = true;
}
if (strlen(urldecode($pluginSettings['DEV_SERVER']))<1){
	WriteSettingToFile("MODE","DEV",$pluginName);
	$madeChange = true;
}
if ($madeChange) {
	$pluginSettings = parse_ini_file($pluginConfigFile);
}

?>

<!DOCTYPE html>
<html>
<head>

</head>
<body>
<div class="pluginBody" style="margin-left: 1em;">
	<div class="title" style="color: black;">
		<h1>megatr.ee callback plugin</h1>
	</div>

<table cellspacing="5">
<tr>
	<th style="text-align: left">Enable Dev Mode</th>
<td>
<?			
	PrintSettingCheckbox("Show On Demand", "show_on_demand_enabled", $restart = 1, $reboot = 0, "true", "false", $pluginName = $pluginName, $callbackName = "", $defaultValue = 0, $desc = "", $sData = Array());
?>
</td>
</tr>


<tr>
	<th style="text-align: left">Dev Server</th>
<td>
<?
//function PrintSettingTextSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "", $inputType = "text", $sData = Array())
	PrintSettingTextSaved("DEV_SERVER", $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>

<tr>
	<th style="text-align: left">Production Server</th>
<td>
<?
//function PrintSettingTextSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "", $inputType = "text", $sData = Array())
	PrintSettingTextSaved("PROD_SERVER", $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>

</table>



</body>
</html>