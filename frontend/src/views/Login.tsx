import { FC } from "react";
import {RegisterForm} from '../components/RegisterForm'
interface ILoginProps {};

export const Login: FC<ILoginProps> = (props) => {
    return (
        <div>
          <RegisterForm/>
        </div>
    );
}
