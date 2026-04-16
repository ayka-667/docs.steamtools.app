# STFixer (aka CloudFix)

Originally, this tool was made to fix broken Capcom game saves caused by SteamTools cloud behavior.  
Now it also fixes several other SteamTools-related issues.

> Disable Steam Cloud for non-owned games in Steam properties.  
> Manually back up your saves for all non-owned games.

## What Is This?

SteamTools modifies Steam Cloud requests to make cloud syncing work for non-owned games.  
This behavior now causes problems, including games using the Steam Screenshots AppID for save operations.

Capcom games are heavily affected: many recent titles may fail to save completely in this state.

STFixer resolves this by disabling the SteamTools cloud "fix", letting Steam Cloud fail normally for non-owned games (as expected), instead of causing save corruption/issues.

It can also:

- Fix other weird SteamTools behaviors
- Install SteamTools even if the backend is down
- Replace the SteamTools manifest endpoint
- Diagnose and repair broken SteamTools installs

## Usage

1. Download `STFixer.exe` from the [latest release](https://github.com/Selectively11/STFixer/releases/latest)
2. Run it
3. Select the patch(es) you want
4. Restart Steam when prompted, or return to the main menu to apply other patches, then restart Steam

To undo changes, run STFixer again and select **Disable (restore originals)**.

If you still get a Capcom save error after enabling STFixer:

1. Disable Steam Cloud for the affected game in Steam properties
2. Clear that game's userdata folder: `<Steam install path>\userdata\<steamid>\<appid>`
3. Restart Steam
4. Try again

## What STFixer Changes

STFixer patches SteamTools DLLs and its encrypted payload cache to improve behavior.

Original files are backed up automatically and can be restored anytime using the Disable option.

## Notes

- STFixer auto-detects your Steam install path from the registry, but you can override it
- Backups are created before any changes
- If SteamTools updates, you may need to run STFixer again
- The tool checks for updates on launch
- SteamTools updates can break this tool, but it is actively maintained
