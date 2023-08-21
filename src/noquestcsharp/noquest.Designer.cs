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
            button1.Location = new Point(12, 347);
            button1.Name = "button1";
            button1.Size = new Size(221, 51);
            button1.TabIndex = 0;
            button1.Text = "Advanced settings";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button2.Location = new Point(326, 347);
            button2.Name = "button2";
            button2.Size = new Size(221, 51);
            button2.TabIndex = 1;
            button2.Text = "Open Oculus Folder";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // button3
            // 
            button3.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button3.Location = new Point(12, 12);
            button3.Name = "button3";
            button3.Size = new Size(151, 51);
            button3.TabIndex = 2;
            button3.Text = "Stop Oculus";
            button3.UseVisualStyleBackColor = true;
            button3.Click += button3_Click;
            // 
            // button4
            // 
            button4.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button4.Location = new Point(169, 12);
            button4.Name = "button4";
            button4.Size = new Size(151, 51);
            button4.TabIndex = 3;
            button4.Text = "Start Oculus";
            button4.UseVisualStyleBackColor = true;
            button4.Click += button4_Click;
            // 
            // button5
            // 
            button5.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button5.Location = new Point(12, 69);
            button5.Name = "button5";
            button5.Size = new Size(151, 51);
            button5.TabIndex = 4;
            button5.Text = "Mirror";
            button5.UseVisualStyleBackColor = true;
            button5.Click += button5_Click;
            // 
            // button6
            // 
            button6.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button6.Location = new Point(169, 69);
            button6.Name = "button6";
            button6.Size = new Size(151, 51);
            button6.TabIndex = 5;
            button6.Text = "Debug Tool";
            button6.UseVisualStyleBackColor = true;
            button6.Click += button6_Click;
            // 
            // button7
            // 
            button7.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button7.Location = new Point(12, 126);
            button7.Name = "button7";
            button7.Size = new Size(151, 51);
            button7.TabIndex = 6;
            button7.Text = "Gather Logs";
            button7.UseVisualStyleBackColor = true;
            button7.Click += button7_Click;
            // 
            // button8
            // 
            button8.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button8.Location = new Point(169, 126);
            button8.Name = "button8";
            button8.Size = new Size(151, 51);
            button8.TabIndex = 7;
            button8.Text = "Fix Drivers";
            button8.UseVisualStyleBackColor = true;
            button8.Click += button8_Click;
            // 
            // label1
            // 
            label1.Font = new Font("Cabin", 16.1999989F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(12, 401);
            label1.Name = "label1";
            label1.Size = new Size(535, 40);
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
            contextMenuStrip1.Font = new Font("Segoe UI", 10.8F, FontStyle.Regular, GraphicsUnit.Point);
            contextMenuStrip1.ImageScalingSize = new Size(20, 20);
            contextMenuStrip1.Items.AddRange(new ToolStripItem[] { showWindowToolStripMenuItem, startOculusToolStripMenuItem, stopOculusToolStripMenuItem, toolsToolStripMenuItem, exitToolStripMenuItem });
            contextMenuStrip1.Name = "contextMenuStrip1";
            contextMenuStrip1.Size = new Size(200, 154);
            // 
            // showWindowToolStripMenuItem
            // 
            showWindowToolStripMenuItem.Name = "showWindowToolStripMenuItem";
            showWindowToolStripMenuItem.Size = new Size(199, 30);
            showWindowToolStripMenuItem.Text = "Show Window";
            showWindowToolStripMenuItem.Click += showWindowToolStripMenuItem_Click;
            // 
            // startOculusToolStripMenuItem
            // 
            startOculusToolStripMenuItem.Name = "startOculusToolStripMenuItem";
            startOculusToolStripMenuItem.Size = new Size(199, 30);
            startOculusToolStripMenuItem.Text = "Start Oculus";
            startOculusToolStripMenuItem.Click += startOculusToolStripMenuItem_Click;
            // 
            // stopOculusToolStripMenuItem
            // 
            stopOculusToolStripMenuItem.Name = "stopOculusToolStripMenuItem";
            stopOculusToolStripMenuItem.Size = new Size(199, 30);
            stopOculusToolStripMenuItem.Text = "Stop Oculus";
            stopOculusToolStripMenuItem.Click += stopOculusToolStripMenuItem_Click;
            // 
            // toolsToolStripMenuItem
            // 
            toolsToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { debugToolToolStripMenuItem, mirrorToolStripMenuItem, logsToolStripMenuItem, driverToolStripMenuItem });
            toolsToolStripMenuItem.Name = "toolsToolStripMenuItem";
            toolsToolStripMenuItem.Size = new Size(199, 30);
            toolsToolStripMenuItem.Text = "Tools";
            // 
            // debugToolToolStripMenuItem
            // 
            debugToolToolStripMenuItem.Name = "debugToolToolStripMenuItem";
            debugToolToolStripMenuItem.Size = new Size(224, 30);
            debugToolToolStripMenuItem.Text = "Debug Tool";
            debugToolToolStripMenuItem.Click += debugToolToolStripMenuItem_Click;
            // 
            // mirrorToolStripMenuItem
            // 
            mirrorToolStripMenuItem.Name = "mirrorToolStripMenuItem";
            mirrorToolStripMenuItem.Size = new Size(224, 30);
            mirrorToolStripMenuItem.Text = "Mirror";
            mirrorToolStripMenuItem.Click += mirrorToolStripMenuItem_Click;
            // 
            // logsToolStripMenuItem
            // 
            logsToolStripMenuItem.Name = "logsToolStripMenuItem";
            logsToolStripMenuItem.Size = new Size(224, 30);
            logsToolStripMenuItem.Text = "Logs";
            logsToolStripMenuItem.Click += logsToolStripMenuItem_Click;
            // 
            // driverToolStripMenuItem
            // 
            driverToolStripMenuItem.Name = "driverToolStripMenuItem";
            driverToolStripMenuItem.Size = new Size(224, 30);
            driverToolStripMenuItem.Text = "Driver";
            driverToolStripMenuItem.Click += driverToolStripMenuItem_Click;
            // 
            // exitToolStripMenuItem
            // 
            exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            exitToolStripMenuItem.Size = new Size(199, 30);
            exitToolStripMenuItem.Text = "Exit";
            exitToolStripMenuItem.Click += exitToolStripMenuItem_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(256, 365);
            label2.Name = "label2";
            label2.Size = new Size(39, 20);
            label2.TabIndex = 9;
            label2.Text = "1.0.0";
            // 
            // noquest
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(559, 450);
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
            MaximumSize = new Size(577, 497);
            MinimumSize = new Size(577, 497);
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