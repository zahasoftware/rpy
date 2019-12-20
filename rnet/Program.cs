using rnet.lib;
using rnet.lib.Implementations;
using System;
using System.Reflection;
using System.Threading.Tasks;

namespace rnet
{
    class Program
    {
        static void Main(string[] args)
        {
            var version = Assembly.GetExecutingAssembly().GetName().Version;
            Console.Write($"Version {version.Major}.{version.Minor}.{version.Revision}.{version.Build}");
            IPyProcess rpyProcess = new rnet.lib.Implementations.Live.LiveProcess(); //or new rnet.lib.Implementations.Live.RPYProcess();

            try
            {
                rpyProcess.Start();

                //ON
                rpyProcess.Switch[18].Write(true);
                Task.Delay(1000).Wait();

                //OFF
                rpyProcess.Switch[18].Write(false);
                Task.Delay(1000).Wait();

                //PWM Increase
                for (int i = 0; i <= 10; i++)
                {
                    rpyProcess.PWM[18].Write(i * 100);
                    Task.Delay(50).Wait();
                }

                //PWM Decrease 
                for (int i = 10; i >= 0; i--)
                {
                    rpyProcess.PWM[18].Write(i * 100);
                    Task.Delay(50).Wait();
                }
            }
            finally
            {
                rpyProcess.Exit();
            }
        }
    }
}
