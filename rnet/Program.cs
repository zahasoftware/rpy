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
            IRPYProcess rpyProcess = new RPYProcess();

            try
            {
                rpyProcess.Start();

                //ON
                rpyProcess.Switch[20].Write(true);
                Task.Delay(1000).Wait();

                //OFF
                rpyProcess.Switch[20].Write(false);
                Task.Delay(1000).Wait();

                //PWM Increase
                for (int i = 0; i <= 10; i++)
                {
                    rpyProcess.PWM[20].Write(i * 10);
                }

                //PWM Decrease 
                for (int i = 10; i >= 0; i--)
                {
                    rpyProcess.PWM[20].Write(i * 10);
                }
            }
            finally
            {
                rpyProcess.Exit();
            }
        }
    }
}
