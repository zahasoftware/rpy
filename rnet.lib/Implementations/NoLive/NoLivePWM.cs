using System;
using System.Collections.Generic;

namespace rnet.lib.Implementations.NoLive
{
    public class NoLivePWM : IPWM
    {
        private NoLiveProcess rpyProcess;
        private readonly int pin;
        private IDictionary<int, NoLivePWM> Pwms { get; } = new Dictionary<int, NoLivePWM>();

        public IPWM this[int pin]
        {
            get
            {
                if (!Pwms.ContainsKey(pin))
                {
                    Pwms[pin] = new NoLivePWM(rpyProcess, pin);
                }
                return Pwms[pin];
            }
        }

        public NoLivePWM(NoLiveProcess rpyProcess)
        {
            this.rpyProcess = rpyProcess;
        }

        public NoLivePWM(NoLiveProcess rpyProcess, int pin)
        {
            this.rpyProcess = rpyProcess;
            this.pin = pin;
        }

        public void Write(int value)
        {
            lock (rpyProcess.@lock)
            {
                Console.WriteLine($"Write {value}");

                var sql = $"pwm pin={pin} value={value}";///Executing command
                rpyProcess.ExcecuteCommand(sql);

                Console.WriteLine($"Stop Waiting {value}");
            }
        }

        public void Write(int value, int frequency)
        {
            lock (rpyProcess.@lock)
            {
                var sql = $"pwm pin={pin} value={value} hertz={frequency}";///Executing command
                rpyProcess.ExcecuteCommand(sql);
            }
        }
    }
}
