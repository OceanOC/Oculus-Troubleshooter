namespace noquestcsharp
{
    partial class noquest
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(noquest));
            button1 = new Button();
            button2 = new Button();
            button3 = new Button();
            button4 = new Button();
            button5 = new Button();
            button6 = new Button();
            button7 = new Button();
            button8 = new Button();
            label1 = new Label();
            notifyIcon1 = new NotifyIcon(components);
            contextMenuStrip1 = new ContextMenuStrip(components);
            showWindowToolStripMenuItem = new ToolStripMenuItem();
            startOculusToolStripMenuItem = new ToolStripMenuItem();
            stopOculusToolStripMenuItem = new ToolStripMenuItem();
            toolsToolStripMenuItem = new ToolStripMenuItem();
            debugToolToolStripMenuItem = new ToolStripMenuItem();
            mirrorToolStripMenuItem = new ToolStripMenuItem();
            logsToolStripMenuItem = new ToolStripMenuItem();
            driverToolStripMenuItem = new ToolStripMenuItem();
            exitToolStripMenuItem = new ToolStripMenuItem();
            label2 = new Label();
            contextMenuStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button1.Location = new Point(10, 260);
            button1.Margin = new Padding(3, 2, 3, 2);
            button1.Name = "button1";
            button1.Size = new Size(193, 38);
            button1.TabIndex = 0;
            button1.Text = "Advanced settings";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button2.Location = new Point(285, 260);
            button2.Margin = new Padding(3, 2, 3, 2);
            button2.Name = "button2";
            button2.Size = new Size(193, 38);
            button2.TabIndex = 1;
            button2.Text = "Open Oculus Folder";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // button3
            // 
            button3.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button3.Location = new Point(10, 9);
            button3.Margin = new Padding(3, 2, 3, 2);
            button3.Name = "button3";
            button3.Size = new Size(132, 38);
            button3.TabIndex = 2;
            button3.Text = "Stop Oculus";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // button4
            // 
            button4.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button4.Location = new Point(148, 9);
            button4.Margin = new Padding(3, 2, 3, 2);
            button4.Name = "button4";
            button4.Size = new Size(132, 38);
            button4.TabIndex = 3;
            button4.Text = "Start Oculus";
            button4.UseVisualStyleBackColor = true;
            button4.Click += button4_Click;
            // 
            // button5
            // 
            button5.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button5.Location = new Point(10, 52);
            button5.Margin = new Padding(3, 2, 3, 2);
            button5.Name = "button5";
            button5.Size = new Size(132, 38);
            button5.TabIndex = 4;
            button5.Text = "Mirror";
            button5.UseVisualStyleBackColor = true;
            button5.Click += button5_Click;
            // 
            // button6
            // 
            button6.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button6.Location = new Point(148, 52);
            button6.Margin = new Padding(3, 2, 3, 2);
            button6.Name = "button6";
            button6.Size = new Size(132, 38);
            button6.TabIndex = 5;
            button6.Text = "Debug Tool";
            button6.UseVisualStyleBackColor = true;
            button6.Click += button6_Click;
            // 
            // button7
            // 
            button7.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button7.Location = new Point(10, 94);
            button7.Margin = new Padding(3, 2, 3, 2);
            button7.Name = "button7";
            button7.Size = new Size(132, 38);
            button7.TabIndex = 6;
            button7.Text = "Gather Logs";
            button7.UseVisualStyleBackColor = true;
            button7.Click += button7_Click;
            // 
            // button8
            // 
            button8.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button8.Location = new Point(148, 94);
            button8.Margin = new Padding(3, 2, 3, 2);
            button8.Name = "button8";
            button8.Size = new Size(132, 38);
            button8.TabIndex = 7;
            button8.Text = "Fix Drivers";
            button8.UseVisualStyleBackColor = true;
            button8.Click += button8_Click;
            // 
            // label1
            // 
            label1.Font = new Font("Cabin", 16.1999989F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(10, 301);
            label1.Name = "label1";
            label1.Size = new Size(468, 30);
            label1.TabIndex = 8;
            label1.Text = "Oculus Troubleshooter";
            label1.TextAlign = ContentAlignment.MiddleCenter;
            label1.Click += label1_Click;
            // 
            // notifyIcon1
            // 
            notifyIcon1.ContextMenuStrip = contextMenuStrip1;
            notifyIcon1.Icon = (Icon)resources.GetObject("notifyIcon1.Icon");
            notifyIcon1.Text = "Oculus Troubleshooter";
            notifyIcon1.Visible = true;
            notifyIcon1.Click += notifyIcon1_Click;
            // 
            // contextMenuStrip1
            // 
            contextMenuStrip1.Font = new Font("Segoe UI", 10.2F, FontStyle.Regular, GraphicsUnit.Point);
            contextMenuStrip1.ImageScalingSize = new Size(20, 20);
            contextMenuStrip1.Items.AddRange(new ToolStripItem[] { showWindowToolStripMenuItem, startOculusToolStripMenuItem, stopOculusToolStripMenuItem, toolsToolStripMenuItem, exitToolStripMenuItem });
            contextMenuStrip1.Name = "contextMenuStrip1";
            contextMenuStrip1.ShowImageMargin = false;
            contextMenuStrip1.Size = new Size(141, 124);
            // 
            // showWindowToolStripMenuItem
            // 
            showWindowToolStripMenuItem.Name = "showWindowToolStripMenuItem";
            showWindowToolStripMenuItem.Size = new Size(140, 24);
            showWindowToolStripMenuItem.Text = "Show Window";
            showWindowToolStripMenuItem.Click += showWindowToolStripMenuItem_Click;
            // 
            // startOculusToolStripMenuItem
            // 
            startOculusToolStripMenuItem.Name = "startOculusToolStripMenuItem";
            startOculusToolStripMenuItem.Size = new Size(140, 24);
            startOculusToolStripMenuItem.Text = "Start Oculus";
            startOculusToolStripMenuItem.Click += startOculusToolStripMenuItem_Click;
            // 
            // stopOculusToolStripMenuItem
            // 
            stopOculusToolStripMenuItem.Name = "stopOculusToolStripMenuItem";
            stopOculusToolStripMenuItem.Size = new Size(140, 24);
            stopOculusToolStripMenuItem.Text = "Stop Oculus";
            stopOculusToolStripMenuItem.Click += stopOculusToolStripMenuItem_Click;
            // 
            // toolsToolStripMenuItem
            // 
            toolsToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { debugToolToolStripMenuItem, mirrorToolStripMenuItem, logsToolStripMenuItem, driverToolStripMenuItem });
            toolsToolStripMenuItem.Name = "toolsToolStripMenuItem";
            toolsToolStripMenuItem.Size = new Size(140, 24);
            toolsToolStripMenuItem.Text = "Tools";
            // 
            // debugToolToolStripMenuItem
            // 
            debugToolToolStripMenuItem.Name = "debugToolToolStripMenuItem";
            debugToolToolStripMenuItem.Size = new Size(148, 24);
            debugToolToolStripMenuItem.Text = "Debug Tool";
            debugToolToolStripMenuItem.Click += debugToolToolStripMenuItem_Click;
            // 
            // mirrorToolStripMenuItem
            // 
            mirrorToolStripMenuItem.Name = "mirrorToolStripMenuItem";
            mirrorToolStripMenuItem.Size = new Size(148, 24);
            mirrorToolStripMenuItem.Text = "Mirror";
            mirrorToolStripMenuItem.Click += mirrorToolStripMenuItem_Click;
            // 
            // logsToolStripMenuItem
            // 
            logsToolStripMenuItem.Name = "logsToolStripMenuItem";
            logsToolStripMenuItem.Size = new Size(148, 24);
            logsToolStripMenuItem.Text = "Logs";
            logsToolStripMenuItem.Click += logsToolStripMenuItem_Click;
            // 
            // driverToolStripMenuItem
            // 
            driverToolStripMenuItem.Name = "driverToolStripMenuItem";
            driverToolStripMenuItem.Size = new Size(148, 24);
            driverToolStripMenuItem.Text = "Driver";
            driverToolStripMenuItem.Click += driverToolStripMenuItem_Click;
            // 
            // exitToolStripMenuItem
            // 
            exitToolStripMenuItem.DisplayStyle = ToolStripItemDisplayStyle.Text;
            exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            exitToolStripMenuItem.Size = new Size(140, 24);
            exitToolStripMenuItem.Text = "Exit";
            exitToolStripMenuItem.Click += exitToolStripMenuItem_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(224, 274);
            label2.Name = "label2";
            label2.Size = new Size(31, 15);
            label2.TabIndex = 9;
            label2.Text = "1.0.0";
            // 
            // noquest
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(491, 344);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(button8);
            Controls.Add(button7);
            Controls.Add(button6);
            Controls.Add(button5);
            Controls.Add(button4);
            Controls.Add(button3);
            Controls.Add(button2);
            Controls.Add(button1);
            Icon = (Icon)resources.GetObject("$this.Icon");
            Margin = new Padding(3, 2, 3, 2);
            MaximumSize = new Size(507, 383);
            MinimumSize = new Size(507, 383);
            Name = "noquest";
            Text = "Oculus Troubleshooter";
            FormClosing += NQ_closing;
            contextMenuStrip1.ResumeLayout(false);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private Button button2;
        private Button button3;
        private Button button4;
        private Button button5;
        private Button button6;
        private Button button7;
        private Button button8;
        private Label label1;
        private NotifyIcon notifyIcon1;
        private Label label2;
        private ContextMenuStrip contextMenuStrip1;
        private ToolStripMenuItem startOculusToolStripMenuItem;
        private ToolStripMenuItem stopOculusToolStripMenuItem;
        private ToolStripMenuItem toolsToolStripMenuItem;
        private ToolStripMenuItem debugToolToolStripMenuItem;
        private ToolStripMenuItem mirrorToolStripMenuItem;
        private ToolStripMenuItem logsToolStripMenuItem;
        private ToolStripMenuItem driverToolStripMenuItem;
        private ToolStripMenuItem exitToolStripMenuItem;
        private ToolStripMenuItem showWindowToolStripMenuItem;
    }
}