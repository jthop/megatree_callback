<?

if (isset($_POST["ReinstallScript"]))
{
$outputReinstallScript = shell_exec(escapeshellcmd("sudo ".$pluginDirectory."/".$_GET['plugin']."/scripts/fpp_install.sh"));
}
?>


<div id="megatree_callback" class="settings">
<fieldset>
<legend>megatr.ee callback plugin</legend>

<!-- last div intentionally skipped to fix footer background -->
