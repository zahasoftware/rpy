using System;
using System.Collections.Generic;

namespace rnet.lib.Implementations.Live
{
    public class LivePWM : IPWM
    {
        private LiveProcess rpyProcess;
        private readonly int pin;
        private IDictionary<int, LivePWM> Pwms { get; } = new Dictionary<int, LivePWM>();

        public IPWM this[int pin]
        {
            get
            {
                if (!Pwms.ContainsKey(pin))
                {
                    Pwms[pin] = new LivePWM(rpyProcess, pin);
                }
                return Pwms[pin];
            }
        }

        public LivePWM(LiveProcess rpyProcess)
        {
            this.rpyProcess = rpyProcess;
        }

        public LivePWM(LiveProcess rpyProcess, int pin)
        {
            this.rpyProcess = rpyProcess;
            this.pin = pin;
        }

        public void Write(int value)
        {
            lock (rpyProcess.@lock)
            {
                Console.WriteLine($"{DateTime.Now:HH:mm:ss} Write {value}");
                rpyProcess.BeginStandardInputWrite();

                rpyProcess.standardInput.WriteLine($"pwm pin={pin} value={value}");///Executing command

                rpyProcess.EndStandardInputWrite();
                Console.WriteLine($"{DateTime.Now:HH:mm:ss} Stop Waiting {value}");
            }
        }

        public void Write(int value, int frequency)
        {
            lock (rpyProcess.@lock)
            {
                rpyProcess.BeginStandardInputWrite();

                rpyProcess.standardInput.WriteLine($"pwm pin={pin} value={value} hertz={frequency}");///Executing command

                rpyProcess.EndStandardInputWrite();
            }
        }
    }
}
