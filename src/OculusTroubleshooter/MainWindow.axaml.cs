using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using System;
using System.Diagnostics;
using System.Windows.Input;

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
            SMenu.Opacity = 0;
            HMenu.Opacity = 0;
            WMenu.Opacity = 0;
        }
        private void RadioButton2_Checked(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            MMenu.Opacity = 0;
            SMenu.Opacity = 1;
            HMenu.Opacity = 0;
            WMenu.Opacity = 0;
        }
        private void RadioButton3_Checked(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            MMenu.Opacity = 0;
            SMenu.Opacity = 0;
            HMenu.Opacity = 1;
            WMenu.Opacity = 0;
        }
        private void RadioButton4_Checked(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            MMenu.Opacity = 0;
            SMenu.Opacity = 0;
            HMenu.Opacity = 0;
            WMenu.Opacity = 1;
        }

        // Open Oculus Folder
        private void openfolder(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            Process.Start("explorer.exe", $"\"{oculusfolder}\"");
        }

        // Apply changes
        private void applychanges(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
        {
            if (ContSleep.IsChecked == true)
            {

            }
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
    }
}