using System;
using System.Collections.Generic;

namespace rnet.lib.Implementations
{
    public class PWM : IPWM
    {
        private RPYProcess rpyProcess;
        private readonly int pin;
        private IDictionary<int, PWM> Pwms { get; } = new Dictionary<int, PWM>();

        public IPWM this[int pin]
        {
            get
            {
                if (!Pwms.ContainsKey(pin))
                {
                    Pwms[pin] = new PWM(rpyProcess, pin);
                }
                return Pwms[pin];
            }
        }

        public PWM(RPYProcess rpyProcess)
        {
            this.rpyProcess = rpyProcess;
        }

        public PWM(RPYProcess rpyProcess, int pin)
        {
            this.rpyProcess = rpyProcess;
            this.pin = pin;
        }

        public void Write(int value)
        {
            lock (rpyProcess.@lock)
            {
                Console.WriteLine($"Write {value}");
                rpyProcess.BeginStandardInputWrite();

                rpyProcess.standardInput.WriteLine($"pwm pin={pin} value={value}");///Executing command

                rpyProcess.EndStandardInputWrite();
                Console.WriteLine($"Stop Waiting {value}");
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
