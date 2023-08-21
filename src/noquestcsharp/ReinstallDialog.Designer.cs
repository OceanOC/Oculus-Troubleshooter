namespace noquestcsharp
{
    partial class ReinstallDialog
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ReinstallDialog));
            button1 = new Button();
            button2 = new Button();
            label1 = new Label();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point);
            button1.Location = new Point(206, 95);
            button1.Name = "button1";
            button1.Size = new Size(94, 37);
            button1.TabIndex = 0;
            button1.Text = "Yes";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point);
            button2.Location = new Point(306, 95);
            button2.Name = "button2";
            button2.Size = new Size(94, 37);
            button2.TabIndex = 1;
            button2.Text = "No";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // label1
            // 
            label1.Font = new Font("Segoe UI", 10.2F, FontStyle.Regular, GraphicsUnit.Point);
            label1.Location = new Point(-1, -2);
            label1.Name = "label1";
            label1.Size = new Size(415, 94);
            label1.TabIndex = 2;
            label1.Text = "Are you sure you would like to reinstall Oculus\r\nIf yes, Press the Repair button on the next window";
            label1.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // ReinstallDialog
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(412, 144);
            Controls.Add(label1);
            Controls.Add(button2);
            Controls.Add(button1);
            Icon = (Icon)resources.GetObject("$this.Icon");
            MaximizeBox = false;
            MaximumSize = new Size(430, 191);
            MinimizeBox = false;
            Name = "ReinstallDialog";
            ShowIcon = false;
            StartPosition = FormStartPosition.CenterScreen;
            Text = "ReinstallDialog";
            TopMost = true;
            ResumeLayout(false);
        }

        #endregion

        private Button button1;
        private Button button2;
        private Label label1;
    }
}