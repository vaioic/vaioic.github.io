# Installing and Setting Up QuPath

[QuPath](https://qupath.github.io/) is an open-source software application for bioimage analysis, specifically designed for quantitative pathology and whole slide image analysis.

---

## 1. System Requirements

Before installing QuPath, ensure your computer meets the following recommended specifications:

* **Operating System:** Windows 10/11 (64-bit), macOS (Intel or Apple Silicon), or 64-bit Linux.
* **RAM:** Minimum 8 GB (16 GB or more recommended for whole slide images).
* **Storage:** SSD recommended for handling large slide files.

---

## 2. Downloading QuPath

1. Navigate to the official [QuPath Releases Page](https://github.com/qupath/qupath/releases/latest).
2. Download the appropriate installer for your platform:
   * **Windows:** `QuPath-v0.5.x-Windows.msi` or `.exe`
   * **macOS:** `QuPath-v0.5.x-macOS.pkg` or `.dmg`
   * **Linux:** `QuPath-v0.5.x-Linux.tar.gz`

---

## 3. Installation Steps

::::{tab-set}

:::{tab-item} Windows
1. Run the downloaded `.msi` file.
2. Follow the setup wizard prompts.
3. Keep the default installation directory unless restricted by system admin policies.
4. Finish installation and launch **QuPath** from your Start Menu.
:::

:::{tab-item} macOS
1. Open the downloaded `.dmg` or `.pkg` installer.
2. Drag the **QuPath** icon into your **Applications** folder.
3. *Note for macOS users:* The first time you launch QuPath, macOS might block it with a security warning. Go to **System Settings $\rightarrow$ Privacy & Security** and click **Open Anyway**.
:::

:::{tab-item} Linux
1. Extract the `.tar.gz` archive:
   ```bash
   tar -xzf QuPath-v0.5.x-Linux.tar.gz
   ```
2. Navigate into the directory and launch the binary executable:
   ```bash
   cd QuPath
   ./bin/QuPath
   ```
:::

::::

---

## 4. Configuring Memory (RAM) Allocation

For large slide analysis or heavy pixel classification tasks, increase QuPath's allocated memory:

1. Launch **QuPath**.
2. Go to **Edit $\rightarrow$ Preferences** in the main menu bar.
3. Find **Maximum memory (MB)** and adjust it:
   * Set this to approximately **75% of your total system RAM** (e.g., set to `12000` MB if your PC has 16 GB RAM).
4. Restart QuPath for changes to take effect.

---

## Next Steps

Once installed, check out our tutorial on [QuPath Pixel Classification Workflows](#) or submit an image analysis consultation request via our [Jira Service Desk Portal](https://varioic.atlassian.net)[cite: 1, 5].