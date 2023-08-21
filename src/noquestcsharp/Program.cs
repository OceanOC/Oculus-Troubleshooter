using System.Diagnostics;

namespace noquestcsharp
{
    internal static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            if (Process.GetProcessesByName("noquestcsharp").Length > 1)
            {
                // Check to make sure only 1 process is running
                MessageBox.Show("This program is already running.");
                Application.Exit();
            }
            else
            {
                Application.Run(new noquest());;
            }
                
        }
    }
}