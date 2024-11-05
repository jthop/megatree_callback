




<!-- last div intentionally skipped to fix footer background -->




<?php


$pluginName = basename(dirname(__FILE__));  //pjd 7-10-2019   added per dkulp 
logEntry("plugin update file: ".$pluginUpdateFile);
$DEBUG = false;

$DEV_SERVER=trim($_POST["DEV_SERVER"]);
$PROD_SERVER=trim($_POST["PROD_SERVER"]);
$MODE=trim($_POST["MODE"]);

if($DEBUG) {
	echo "PORT: ".$_POST['PORT'];//print_r($_POST["PORT"]);
	echo "loop message: ".$_POST["LOOPMESSAGE"]."<br/> \n";
}

if(isset($_POST['submit']))
{

//	echo "Writring config fie <br/> \n";

	WriteSettingToFile("DEV_SERVER",$DEV_SERVER,$pluginName);
	WriteSettingToFile("PROD_SERVER",$PROD_SERVER,$pluginName);
	WriteSettingToFile("MODE",$MODE,$pluginName);
} else {
	$DEV_SERVER = $pluginSettings['DEV_SERVER'];
	$PROD_SERVER = $pluginSettings['PROD_SERVER'];
	$MODE = $pluginSettings['MODE'];
}

if(isset($_POST['updatePlugin']))
{
	logEntry("updating plugin...");
	$updateResult = updatePluginFromGitHub($gitURL, $branch="master", $pluginName);

	echo $updateResult."<br/> \n";
}

?>

<html>
<head>
</head>

<div id="megatree_callback" class="settings">
    
<fieldset>
<legend>megatr.ee callback plugin</legend>

<form method="post" action="http://<? echo $_SERVER['SERVER_ADDR'].":".$_SERVER['SERVER_PORT']?>/plugin.php?plugin=<?php echo $pluginName;?>&page=plugin_setup.php">

    <?php 
echo "ENABLE PLUGIN: ";

if($ENABLED == "on" || $ENABLED == 1) {
		echo "<input type=\"checkbox\" checked name=\"ENABLED\"> \n";
} else {
		echo "<input type=\"checkbox\"  name=\"ENABLED\"> \n";
}
echo "<p/> \n";

?>
Dev Server: <input type="text" name="dev"><br>
Prod Server: <input type="text" name="prod"><br>
Mode: <input type="text" name="mode"><br>

<input type="submit">
</form>
</fieldset>
</div>
<br />
</html>
