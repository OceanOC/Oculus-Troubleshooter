using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using MsBox.Avalonia.Enums;
using MsBox.Avalonia;
using System;
using System.Diagnostics;
using System.Security.Principal;
using System.Windows.Input;
using Tmds.DBus.Protocol;

namespace OculusTroubleshooter
{
    public partial class MainWindow : Window
    {
        private string oculusfolder = Environment.ExpandEnvironmentVariables("%OculusBase%");

        

        public MainWindow()
        {
            InitializeComponent();
            
        }

        // This is the worst way of doing transition but im too lazy to make if's

        private void RadioButton_Checked(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            MMenu.Opacity = 1;
            WMenu.Opacity = 0;
        }
        private void RadioButton4_Checked(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            MMenu.Opacity = 0;
            WMenu.Opacity = 1;
        }

        // Open Oculus Folder
        private void openfolder(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            Process.Start("explorer.exe", $"\"{oculusfolder}\"");
        }

        // Disable/Enable USB Selective Suspend
        private void DisableSleep(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            // This is one of the worst ways of changeing powercfg but theres no other way in C#
            if (DisableS.IsChecked == true)
            {
                Process.Start("powercfg", "/SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 0​");
            }
            else
            {
                Process.Start("powercfg", "/SETDCVALUEINDEX SCHEME_CURRENT 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1​");
            }
        }

        // Stop Oculus Service
        private void StartOculus(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/C net start OVRService";
            process.StartInfo = startInfo;
            process.Start();
        }

        // Start Oculus Service
        private void StopOculus(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
            startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "/C net stop OVRService";
            process.StartInfo = startInfo;
            process.Start();
        }

        // Oculus Debug Tool
        private void DebugTool(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            Process.Start(oculusfolder + @"\Support\oculus-diagnostics\OculusDebugTool.exe");
        }

        // Gather Logs
        private void Logs(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            Process.Start(oculusfolder + @"\Support\oculus-diagnostics\OculusLogGatherer.exe");
        }

        // Oculus Mirror
        private void Mirror(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            Process.Start(oculusfolder + @"\Support\oculus-diagnostics\OculusMirror.exe");
        }

        // Fix Drivers
        private void Drivers(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            Process.Start(oculusfolder + @"\Support\oculus-drivers\oculus-driver.exe");
        }
        private void PwrPlan(object? sender, SelectionChangedEventArgs e)
        {
            bool isElevated;
            using (WindowsIdentity identity = WindowsIdentity.GetCurrent())
            {
                WindowsPrincipal principal = new WindowsPrincipal(identity);
                isElevated = principal.IsInRole(WindowsBuiltInRole.Administrator);
            }
            if (PowerCombo != null)
            {
                
            if (PowerCombo.SelectedIndex == 0)
            {
                if (isElevated)
                {
                    Process.Start("powercfg", "/s 381b4222-f694-41f0-9685-ff5bb260df2e");
                }
                    else
                    {
                        var box = MessageBoxManager.GetMessageBoxStandard("Error", "Please restart the program with administrator permissions.", ButtonEnum.Ok);
                        box.ShowAsync();
                    }
                } 
            else if (PowerCombo.SelectedIndex == 1)
            {
                if (isElevated)
                {
                    Process.Start("powercfg", "/s 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c");
                } else
                {
                        var box = MessageBoxManager.GetMessageBoxStandard("Error", "Please restart the program with administrator permissions.", ButtonEnum.Ok);
                        box.ShowAsync();
                }
                } 
            else if (PowerCombo.SelectedIndex == 2)
            {
                if (isElevated)
                {
                    Process.Start("powercfg", "/s a1841308-3541-4fab-bc81-f71556f20b4a");
                } else
                {
                    var box = MessageBoxManager.GetMessageBoxStandard("Error", "Please restart the program with administrator permissions.",ButtonEnum.Ok);
                    box.ShowAsync();
                }
            }

            }
        }


        private void Credits(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            var m = new CreditWindow();
            m.Show();
        }
    }
}