# Installing QuPath

## Download the installer

1. Navigate to the official [QuPath releases website](https://github.com/qupath/qupath/releases).

2. Download the appropriate installer for your platform. For your convenience, the
   v0.7.0 links are provided here:

   ```{tab} Windows
   Download the ``.msi`` file:

   * [QuPath-v0.7.0-Windows.msi](https://github.com/qupath/qupath/releases/download/v0.7.0/QuPath-v0.7.0-Windows.msi)

   ```

   ```{tab} macOS
   We recommend installing the Intel version of QuPath as it has better compatibility with the Zeiss CZI-files. Download the ``.pkg`` file:

   * [QuPath-v0.7.0-Mac-x64](https://github.com/qupath/qupath/releases/download/v0.7.0/QuPath-v0.7.0-Mac-x64.pkg)
   ```

   ```{tab} Linux
   Download the linux ``.tar.gz`` file:

   * [QuPath-v0.7.0-Linux.tar.xz](https://github.com/qupath/qupath/releases/download/v0.7.0/QuPath-v0.7.0-Linux.tar.xz)
   ```

## Installation

```{tab} Windows
1. Run the downloaded `.msi` file.
2. Follow the setup wizard prompts.
3. Keep the default installation directory unless restricted by system admin policies.
4. Finish installation and launch **QuPath** from your Start Menu.
```

```{tab} macOS
1. Open the downloaded installer. You will see a warning saying that the file cannot be opened (see image below). **DO NOT CLICK ON THE BLUE BUTTON**. Click on **Done**.

   ![QuPath Installation Step 3](/_images/qupath/qupath_install_step_3.png)

2. Open **Settings** then find **Privacy & Security** on the left panel.

3. Scroll down to the **Security** section. You should see a warning that the QuPath installer was blocked. Click on **Open Anyway**.

   ![QuPath Installation Step 4](/_images/qupath/qupath_install_step_4.png)

4. A popup should appear. Click on **Open Anyway**.

   ![QuPath Installation Step 5](/_images/qupath/qupath_install_step_5.png)

5. The installation wizard should appear. Click through the wizard to install QuPath.

   ![QuPath Installation Step 6](/_images/qupath/qupath_install_step_6.png)

   ![QuPath Installation Step 7](/_images/qupath/qupath_install_step_7.png)

   ![QuPath Installation Step 8](/_images/qupath/qupath_install_step_8.png)

6. Launch QuPath by searching for it using Finder (Cmd + Spacebar)

   ![QuPath Installation Step 9](/_images/qupath/qupath_install_step_9.png)
```

`````{tab} Linux
1. Extract the `.tar.gz` archive:
   ```bash
   tar -xzf QuPath-v0.5.x-Linux.tar.gz
   ```
2. Navigate into the directory and launch the binary executable:
   ```bash
   cd QuPath
   ./bin/QuPath
   ```
`````

## Tips and tricks

```{dropdown} Stop popups when starting QuPath

QuPath has a number of popups that appear on start up. If you want to stop them from
appearing each time:

1. In the first popup, check the box that says **Don't show this again (always
   accept)**.
   
   ![QuPath auto-accept popup](/_images/qupath/qupath_install_step_10.png)

2. In the second popup, uncheck the box that says **Show this on startup** (bottom left)

3. Finally, uncheck the box that says **Remind me next time**.
   
   ![QuPath do not remind](/_images/qupath/qupath_install_step_12.png)
```

```{dropdown} Configuring Memory (RAM) Allocation

For large slide analysis or heavy pixel classification tasks, you may need to increase QuPath's allocated memory:

1. Launch **QuPath**.
2. Go to **Edit** &rarr; **Preferences** in the main menu bar to open the Preferences panel.
3. Go to **General**, then adjust the **Set max memory** setting:
   * Set this to approximately **75% of your total system RAM** (e.g., set to `12000` MB if your PC has 16 GB RAM).
4. Close the panel. Then restart QuPath for changes to take effect.

  ![QuPath set memory](/_images/qupath/qupath_tips_1.png)
```