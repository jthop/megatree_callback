<?
$outputGPIOReset = "";
if (isset($_POST["GPIOResetButton"]))
{
$outputGPIOReset = shell_exec(escapeshellcmd("sudo ".$pluginDirectory."/".$_GET['plugin']."/callbacks.py --reset"));
}
$outputReinstallScript;
if (isset($_POST["ReinstallScript"]))
{
$outputReinstallScript = shell_exec(escapeshellcmd("sudo ".$pluginDirectory."/".$_GET['plugin']."/scripts/fpp_install.sh"));
}
?>

<script type="text/javascript">
<!--
    function toggle(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
    }
//-->
</script>

<div id="megatree_callback" class="settings">
<fieldset>
<legend>megatr.ee callback plugin</legend>

<!-- last div intentionally skipped to fix footer background -->
