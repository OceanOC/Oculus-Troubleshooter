using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Collections;
using System;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.DataFormats;

namespace noquestcsharp
{

    public partial class noquest : Form
    {
        public string oculuspath = Environment.GetEnvironmentVariable("OculusBase");
        public noquest()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            advanced newForm = new advanced();
            newForm.Show();
        }
        private void button2_Click(object sender, EventArgs e)
        {
            // Oculus Folder
            Process process = new Process();
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = @"/C explorer " + oculuspath;
            process.StartInfo = startInfo;
            process.Start();
        }
        private void button3_Click(object sender, EventArgs e)
        {
            Process process = new Process();
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = @"/C net stop OVRService";
            process.StartInfo = startInfo;
            process.Start();
        }
        private void button4_Click(object sender, EventArgs e)
        {
            Process process = new Process();
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = @"/C net start OVRService";
            process.StartInfo = startInfo;
            process.Start();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            // Mirror
            Process process = new Process();
            process.StartInfo.FileName = @oculuspath + @"Support\oculus-diagnostics\OculusMirror.exe";
            process.Start();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // Debug Tool
            Process process = new Process();
            process.StartInfo.FileName = oculuspath + @"Support\oculus-diagnostics\OculusDebugTool.exe";
            process.Start();
        }
        private void button7_Click(object sender, EventArgs e)
        {
            // Make Logs
            Process process = new Process();
            process.StartInfo.FileName = oculuspath + @"Support\oculus-diagnostics\OculusLogGatherer.exe";
            process.Start();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            // Fix Driver
            Process process = new Process();
            process.StartInfo.FileName = oculuspath + @"Support\oculus-drivers\oculus-driver.exe";
            process.Start();
        }

        private void label1_Click(object sender, EventArgs e)
        {
            // This is just for debugging
            Debug.WriteLine(oculuspath);
        }

        private void NQ_closing(object sender, FormClosingEventArgs e)
        {
            e.Cancel = true;
            this.Hide();
        }

        private void notifyIcon1_Click(object sender, EventArgs e)
        {
            MouseEventArgs me = (MouseEventArgs)e;
            if (me.Button == MouseButtons.Left)
            {
                this.Show();
            }
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Dispose(); this.Close();
        }

        private void showWindowToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Show();
        }

        private void startOculusToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button4_Click(sender, e);
        }

        private void stopOculusToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button3_Click(sender, e);
        }

        private void debugToolToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button6_Click(sender, e);
        }

        private void mirrorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button5_Click(sender, e);
        }

        private void logsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button7_Click(sender, e);
        }

        private void driverToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button8_Click(sender, e);
        }
    }
}
