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
	<div class="title">
		<h1>megatr.ee</h1>
		<h4></h4>
	</div>

<p>Press F1 for setup instructions</p>
<table cellspacing="5">
<tr>
	<th style="text-align: left">Enable Show On Demand</th>
<td>
<?			
	PrintSettingCheckbox("Show On Demand", "show_on_demand_enabled", $restart = 1, $reboot = 0, "true", "false", $pluginName = $pluginName, $callbackName = "", $defaultValue = 0, $desc = "", $sData = Array());
?>
</td>
</tr>


<tr>
	<th style="text-align: left">Voip.ms API Username</th>
<td>
<?
//function PrintSettingTextSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "", $inputType = "text", $sData = Array())
	PrintSettingTextSaved("voipms_api_username", $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>

<tr>
	<th style="text-align: left">Voip.ms API Password</th>
<td>
<?
//function PrintSettingPasswordSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "")
	PrintSettingPasswordSaved("voipms_api_password", $restart = 1, $reboot = 0, $maxlength = 50, $size = 32, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>


<tr>
	<th style="text-align: left">Start Command</th>
<td>
<?
//function PrintSettingTextSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "", $inputType = "text", $sData = Array())
	PrintSettingTextSaved("start_command", $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>

<tr>
	<th style="text-align: left">Success Message</th>
<td>
<?
//function PrintSettingTextSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "", $inputType = "text", $sData = Array())
	PrintSettingTextSaved("message_success", $restart = 1, $reboot = 0, $maxlength = 160, $size = 100, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>


<tr>
	<th style="text-align: left">Not started message</th>
<td>
<?
//function PrintSettingTextSaved($setting, $restart = 1, $reboot = 0, $maxlength = 32, $size = 32, $pluginName = "", $defaultValue = "", $callbackName = "", $changedFunction = "", $inputType = "text", $sData = Array())
	PrintSettingTextSaved("message_not_started", $restart = 1, $reboot = 0, $maxlength = 160, $size = 100, $pluginName = $pluginName, $defaultValue = "");
?>
</td>
</tr>

<tr>
	<th style="text-align: left">On-Demand Playlist</th>
<td>
<?
	// function PrintSettingSelect($title, $setting, $restart = 1, $reboot = 0, $defaultValue, $values, $pluginName = "", $callbackName = "", $changedFunction = "", $sData = Array())
	PrintSettingSelect("On-Demand Playlist", "on_demand_playlist", $restart = 1, $reboot = 0, "", $playlists, $pluginName);
?>
</td>
</tr>

<tr>
	<th style="text-align: left">Show Playlist</th>
<td>
<?
	PrintSettingSelect("Show Playlist", "main_playlist", $restart = 1, $reboot = 0, "", $playlists, $pluginName);
?>
</td>
</tr>

</table>



</body>
</html>